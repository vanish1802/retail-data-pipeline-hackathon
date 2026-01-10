import os
import sys

# Add project root to Python path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

import psycopg2
from config.db_config import DB_CONFIG

def test_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    cur.execute("SELECT version();")
    version = cur.fetchone()

    print("Connected to PostgreSQL")
    print("DB version:", version)

    cur.close()
    conn.close()

if __name__ == "__main__":
    test_connection()
