import psycopg2
from config.db_config import DB_CONFIG
import json
from datetime import date, datetime
from decimal import Decimal


from datetime import date, datetime

def make_json_safe(record: dict):
    """
    Convert non-JSON-serializable Python objects
    (datetime, date, Decimal) into safe representations.
    """
    safe_record = {}

    for key, value in record.items():
        if isinstance(value, (datetime, date)):
            safe_record[key] = value.isoformat()
        elif isinstance(value, Decimal):
            safe_record[key] = float(value)
        else:
            safe_record[key] = value

    return safe_record



def quarantine_record(cur, source_table, record, reason):
    cur.execute(
        """
        INSERT INTO staging.quarantine_records
        (source_table, record_data, error_reason)
        VALUES (%s, %s, %s)
        """,
        (source_table, json.dumps(make_json_safe(record)), reason)
    )

    

def main():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    # Load valid store IDs
    cur.execute("SELECT store_id FROM raw.stores")
    valid_stores = {row[0] for row in cur.fetchall()}

    # Load headers
    cur.execute("SELECT * FROM raw.store_sales_header")
    header_cols = [desc[0] for desc in cur.description]
    headers = [dict(zip(header_cols, row)) for row in cur.fetchall()]

    # Load line items
    cur.execute("SELECT * FROM raw.store_sales_line_items")
    line_cols = [desc[0] for desc in cur.description]
    lines = [dict(zip(line_cols, row)) for row in cur.fetchall()]

    # Group line items by transaction
    line_map = {}
    for line in lines:
        tid = line["transaction_id"]
        line_map.setdefault(tid, []).append(line)

    for header in headers:
        tid = header["transaction_id"]
        store_id = header["store_id"]

        # Rule: invalid store
        if store_id not in valid_stores:
            quarantine_record(cur, "store_sales_header", header, "Invalid store_id")
            continue

        related_lines = line_map.get(tid, [])
        calculated_total = 0
        valid_lines = []

        for line in related_lines:
            # Rule: missing product_id
            if not line["product_id"]:
                quarantine_record(cur, "store_sales_line_items", line, "Missing product_id")
                continue

            # Rule: negative amount
            if line["line_item_amount"] < 0:
                quarantine_record(cur, "store_sales_line_items", line, "Negative line_item_amount")
                continue

            calculated_total += line["line_item_amount"]
            valid_lines.append(line)

        # Rule: header total mismatch
        if round(calculated_total, 2) != round(header["total_amount"], 2):
            quarantine_record(
                cur,
                "store_sales_header",
                header,
                "Header total does not match sum of line items"
            )
            continue

        # Insert clean header
        cur.execute(
            """
            INSERT INTO staging.store_sales_header
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                header["transaction_id"],
                header["customer_id"],
                header["store_id"],
                header["transaction_date"],
                header["total_amount"],
            )
        )

        # Insert clean lines
        for line in valid_lines:
            cur.execute(
                """
                INSERT INTO staging.store_sales_line_items
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    line["line_item_id"],
                    line["transaction_id"],
                    line["product_id"],
                    line["promotion_id"],
                    line["quantity"],
                    line["line_item_amount"],
                )
            )

    conn.commit()
    cur.close()
    conn.close()

    print("Validation complete: clean data in staging, bad data quarantined.")

if __name__ == "__main__":
    main()
