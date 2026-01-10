import psycopg2
from config.db_config import DB_CONFIG

def main():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    # Step 1: promoted revenue per promotion & category
    cur.execute("""
        SELECT
            li.promotion_id,
            p.product_category,
            SUM(li.line_item_amount) AS promo_revenue
        FROM staging.store_sales_line_items li
        JOIN raw.products p
            ON li.product_id = p.product_id
        WHERE li.promotion_id IS NOT NULL
        GROUP BY li.promotion_id, p.product_category
    """)
    promo_rows = cur.fetchall()

    # Step 2: baseline revenue per category (no promotion)
    cur.execute("""
        SELECT
            p.product_category,
            SUM(li.line_item_amount) AS baseline_revenue
        FROM staging.store_sales_line_items li
        JOIN raw.products p
            ON li.product_id = p.product_id
        WHERE li.promotion_id IS NULL
        GROUP BY p.product_category
    """)
    baseline_map = {
        row[0]: row[1] for row in cur.fetchall()
    }

    results = []

    for promo_id, category, promo_revenue in promo_rows:
        baseline_revenue = baseline_map.get(category, 0)

        if baseline_revenue and baseline_revenue > 0:
            lift_pct = ((promo_revenue - baseline_revenue) / baseline_revenue) * 100
        else:
            lift_pct = None  # undefined lift

        results.append({
            "promotion_id": promo_id,
            "category": category,
            "promo_revenue": round(promo_revenue, 2),
            "baseline_revenue": round(baseline_revenue, 2) if baseline_revenue else 0,
            "lift_pct": round(lift_pct, 2) if lift_pct is not None else None
        })

    # Step 3: sort by lift
    results = sorted(
        results,
        key=lambda x: (x["lift_pct"] is not None, x["lift_pct"]),
        reverse=True
    )

    print("\nTop Promotion Effectiveness Report\n")
    for r in results[:3]:
        print(
            f"Promotion {r['promotion_id']} | "
            f"Category: {r['category']} | "
            f"Promo Revenue: {r['promo_revenue']} | "
            f"Baseline Revenue: {r['baseline_revenue']} | "
            f"Lift %: {r['lift_pct']}"
        )

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
