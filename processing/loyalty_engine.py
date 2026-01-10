import psycopg2
from config.db_config import DB_CONFIG

def main():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    # Load loyalty rules
    cur.execute("""
        SELECT rule_id, points_per_unit_spend, min_spend_threshold, bonus_points
        FROM raw.loyalty_rules
    """)
    rules = cur.fetchall()

    # Load transactions
    cur.execute("""
        SELECT transaction_id, customer_id, total_amount, transaction_date
        FROM staging.store_sales_header
    """)
    transactions = cur.fetchall()

    for txn_id, customer_id, amount, txn_date in transactions:
        earned_points = 0

        for rule_id, rate, min_spend, bonus in rules:
            if amount >= min_spend:
                earned_points += int(amount * rate)
                earned_points += bonus

        # Update customer points and last purchase date
        cur.execute("""
            UPDATE raw.customer_details
            SET total_loyalty_points = total_loyalty_points + %s,
                last_purchase_date = %s
            WHERE customer_id = %s
        """, (earned_points, txn_date, customer_id))

    conn.commit()
    cur.close()
    conn.close()

    print("Loyalty points calculated and updated successfully.")

if __name__ == "__main__":
    main()
