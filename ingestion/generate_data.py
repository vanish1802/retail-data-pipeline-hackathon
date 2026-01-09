"""
Synthetic data generator for Retail Data Pipeline
Generates relationally consistent CSV files with injected anomalies
"""

import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

# Output directory
RAW_DATA_DIR = Path("data/raw")
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

def generate_stores():
    stores = [
        {
            "store_id": "S001",
            "store_name": "HCL Mart Indore",
            "store_city": "Indore",
            "store_region": "Madhya Pradesh",
            "opening_date": "2018-05-10"
        },
        {
            "store_id": "S002",
            "store_name": "HCL Mart Pune",
            "store_city": "Pune",
            "store_region": "Maharashtra",
            "opening_date": "2019-08-15"
        },
        {
            "store_id": "S003",
            "store_name": "HCL Mart Bengaluru",
            "store_city": "Bengaluru",
            "store_region": "Karnataka",
            "opening_date": "2021-01-20"
        }
    ]

    file_path = RAW_DATA_DIR / "stores.csv"

    with open(file_path, mode="w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "store_id",
                "store_name",
                "store_city",
                "store_region",
                "opening_date"
            ]
        )
        writer.writeheader()
        writer.writerows(stores)

    print(f"Generated {len(stores)} records in {file_path}")


def generate_products():
    products = [
        {"product_id": "P001", "product_name": "Smartphone", "product_category": "Electronics", "unit_price": 15000.00, "current_stock_level": 50},
        {"product_id": "P002", "product_name": "Laptop", "product_category": "Electronics", "unit_price": 55000.00, "current_stock_level": 30},
        {"product_id": "P003", "product_name": "Headphones", "product_category": "Electronics", "unit_price": 2000.00, "current_stock_level": 100},

        {"product_id": "P004", "product_name": "T-Shirt", "product_category": "Apparel", "unit_price": 800.00, "current_stock_level": 200},
        {"product_id": "P005", "product_name": "Jeans", "product_category": "Apparel", "unit_price": 1800.00, "current_stock_level": 120},
        {"product_id": "P006", "product_name": "Jacket", "product_category": "Apparel", "unit_price": 3500.00, "current_stock_level": 60},

        {"product_id": "P007", "product_name": "Rice (5kg)", "product_category": "Grocery", "unit_price": 400.00, "current_stock_level": 300},
        {"product_id": "P008", "product_name": "Cooking Oil (1L)", "product_category": "Grocery", "unit_price": 180.00, "current_stock_level": 250},
        {"product_id": "P009", "product_name": "Sugar (1kg)", "product_category": "Grocery", "unit_price": 50.00, "current_stock_level": 500},
        {"product_id": "P010", "product_name": "Tea Pack", "product_category": "Grocery", "unit_price": 120.00, "current_stock_level": 400},
    ]

    file_path = RAW_DATA_DIR / "products.csv"

    with open(file_path, mode="w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "product_id",
                "product_name",
                "product_category",
                "unit_price",
                "current_stock_level"
            ]
        )
        writer.writeheader()
        writer.writerows(products)

    print(f"Generated {len(products)} records in {file_path}")


def generate_customers():
    today = datetime.today().date()

    customers = [
        {
            "customer_id": "C001",
            "first_name": "Amit",
            "email": "amit@example.com",
            "loyalty_status": "Gold",
            "total_loyalty_points": 1200,
            "last_purchase_date": today - timedelta(days=5),
            "segment_id": ""
        },
        {
            "customer_id": "C002",
            "first_name": "Neha",
            "email": "neha@example.com",
            "loyalty_status": "Silver",
            "total_loyalty_points": 600,
            "last_purchase_date": today - timedelta(days=12),
            "segment_id": ""
        },
        {
            "customer_id": "C003",
            "first_name": "Ravi",
            "email": "ravi@example.com",
            "loyalty_status": "Bronze",
            "total_loyalty_points": 150,
            "last_purchase_date": today - timedelta(days=65),
            "segment_id": ""
        },
        {
            "customer_id": "C004",
            "first_name": "Pooja",
            "email": "pooja@example.com",
            "loyalty_status": "Bronze",
            "total_loyalty_points": 300,
            "last_purchase_date": today - timedelta(days=90),
            "segment_id": ""
        },
        {
            "customer_id": "C005",
            "first_name": "Karan",
            "email": "karan@example.com",
            "loyalty_status": "Gold",
            "total_loyalty_points": 2000,
            "last_purchase_date": today - timedelta(days=2),
            "segment_id": ""
        },
    ]

    file_path = RAW_DATA_DIR / "customer_details.csv"

    with open(file_path, mode="w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "customer_id",
                "first_name",
                "email",
                "loyalty_status",
                "total_loyalty_points",
                "last_purchase_date",
                "segment_id"
            ]
        )
        writer.writeheader()
        writer.writerows(customers)

    print(f"Generated {len(customers)} records in {file_path}")


def generate_promotions():
    today = datetime.today().date()

    promotions = [
        {
            "promotion_id": "PR001",
            "promotion_name": "Electronics New Year Sale",
            "start_date": today - timedelta(days=10),
            "end_date": today + timedelta(days=10),
            "discount_percentage": 0.10,
            "applicable_category": "Electronics"
        },
        {
            "promotion_id": "PR002",
            "promotion_name": "Apparel Clearance",
            "start_date": today - timedelta(days=20),
            "end_date": today - timedelta(days=1),
            "discount_percentage": 0.20,
            "applicable_category": "Apparel"
        },
        {
            "promotion_id": "PR003",
            "promotion_name": "Grocery Weekend Offer",
            "start_date": today - timedelta(days=5),
            "end_date": today + timedelta(days=5),
            "discount_percentage": 0.05,
            "applicable_category": "Grocery"
        }
    ]

    file_path = RAW_DATA_DIR / "promotion_details.csv"

    with open(file_path, mode="w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "promotion_id",
                "promotion_name",
                "start_date",
                "end_date",
                "discount_percentage",
                "applicable_category"
            ]
        )
        writer.writeheader()
        writer.writerows(promotions)

    print(f"Generated {len(promotions)} records in {file_path}")


def generate_loyalty_rules():
    rules = [
        {
            "rule_id": 1,
            "rule_name": "Standard Earning",
            "points_per_unit_spend": 1.0,
            "min_spend_threshold": 0.0,
            "bonus_points": 0
        },
        {
            "rule_id": 2,
            "rule_name": "High Value Bonus",
            "points_per_unit_spend": 1.0,
            "min_spend_threshold": 5000.0,
            "bonus_points": 50
        }
    ]

    file_path = RAW_DATA_DIR / "loyalty_rules.csv"

    with open(file_path, mode="w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "rule_id",
                "rule_name",
                "points_per_unit_spend",
                "min_spend_threshold",
                "bonus_points"
            ]
        )
        writer.writeheader()
        writer.writerows(rules)

    print(f"Generated {len(rules)} records in {file_path}")


def generate_sales_data():
    headers = []
    line_items = []

    transaction_counter = 1
    line_item_counter = 1
    today = datetime.today()

    store_ids = ["S001", "S002", "S003"]
    customer_ids = ["C001", "C002", "C003", "C004", "C005"]
    product_ids = ["P001", "P002", "P003", "P004", "P005", "P006", "P007", "P008", "P009", "P010"]
    promotion_ids = ["PR001", "PR002", "PR003", None]

    for day in range(7):
        transaction_date = today - timedelta(days=day)

        for _ in range(3):  # 3 transactions per day
            transaction_id = f"T{transaction_counter:04d}"
            transaction_counter += 1

            store_id = random.choice(store_ids)
            customer_id = random.choice(customer_ids)

            num_items = random.randint(1, 3)
            total_amount = 0

            for _ in range(num_items):
                product_id = random.choice(product_ids)
                quantity = random.randint(1, 3)
                unit_price = random.randint(50, 5000)
                amount = unit_price * quantity

                # Inject anomaly: negative amount
                if random.random() < 0.05:
                    amount = -amount

                promotion_id = random.choice(promotion_ids)

                line_items.append({
                    "line_item_id": line_item_counter,
                    "transaction_id": transaction_id,
                    "product_id": product_id if random.random() > 0.05 else "",
                    "promotion_id": promotion_id,
                    "quantity": quantity,
                    "line_item_amount": amount
                })

                line_item_counter += 1
                total_amount += amount

            # Inject anomaly: wrong total
            if random.random() < 0.1:
                total_amount += random.randint(100, 500)

            headers.append({
                "transaction_id": transaction_id,
                "customer_id": customer_id,
                "store_id": store_id if random.random() > 0.05 else "INVALID",
                "transaction_date": transaction_date,
                "total_amount": round(total_amount, 2)
            })

    # Write header CSV
    header_path = RAW_DATA_DIR / "store_sales_header.csv"
    with open(header_path, mode="w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "transaction_id",
                "customer_id",
                "store_id",
                "transaction_date",
                "total_amount"
            ]
        )
        writer.writeheader()
        writer.writerows(headers)

    # Write line items CSV
    line_item_path = RAW_DATA_DIR / "store_sales_line_items.csv"
    with open(line_item_path, mode="w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "line_item_id",
                "transaction_id",
                "product_id",
                "promotion_id",
                "quantity",
                "line_item_amount"
            ]
        )
        writer.writeheader()
        writer.writerows(line_items)

    print(f"Generated {len(headers)} transactions and {len(line_items)} line items")


if __name__ == "__main__":
    generate_stores()
    generate_products()
    generate_customers()
    generate_promotions()
    generate_loyalty_rules()
    generate_sales_data()
