import csv
from pathlib import Path
import psycopg2
from config.db_config import DB_CONFIG

RAW_DATA_DIR = Path("data/raw")

TABLE_MAPPING = {
    "stores.csv": "raw.stores",
    "products.csv": "raw.products",
    "customer_details.csv": "raw.customer_details",
    "promotion_details.csv": "raw.promotion_details",
    "loyalty_rules.csv": "raw.loyalty_rules",
    "store_sales_header.csv": "raw.store_sales_header",
    "store_sales_line_items.csv": "raw.store_sales_line_items",
}

def ingest_csv(file_name, table_name, conn):
    file_path = RAW_DATA_DIR / file_name

    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        columns = reader.fieldnames

        placeholders = ", ".join(["%s"] * len(columns))
        column_names = ", ".join(columns)

        insert_query = f"""
            INSERT INTO {table_name} ({column_names})
            VALUES ({placeholders})
        """

        cur = conn.cursor()

        for row in reader:
            values = [row[col] if row[col] != "" else None for col in columns]
            cur.execute(insert_query, values)

        conn.commit()
        cur.close()

        print(f"Ingested {file_name} into {table_name}")

def main():
    conn = psycopg2.connect(**DB_CONFIG)

    for file_name, table_name in TABLE_MAPPING.items():
        ingest_csv(file_name, table_name, conn)

    conn.close()

if __name__ == "__main__":
    main()
