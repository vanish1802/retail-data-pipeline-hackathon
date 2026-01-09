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
    pass

def generate_customers():
    pass

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
