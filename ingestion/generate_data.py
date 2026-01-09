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
    pass

def generate_loyalty_rules():
    pass

def generate_sales_data():
    pass

if __name__ == "__main__":
    generate_stores()
    generate_products()
    generate_customers()
    generate_promotions()
    generate_loyalty_rules()
    generate_sales_data()
