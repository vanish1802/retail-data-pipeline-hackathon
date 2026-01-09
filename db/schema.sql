-- =========================
-- SCHEMAS
-- =========================

CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS staging;

-- =========================
-- RAW TABLES (NO CONSTRAINTS)
-- =========================

CREATE TABLE IF NOT EXISTS raw.stores (
    store_id VARCHAR(10),
    store_name VARCHAR(100),
    store_city VARCHAR(50),
    store_region VARCHAR(50),
    opening_date DATE
);

CREATE TABLE IF NOT EXISTS raw.products (
    product_id VARCHAR(20),
    product_name VARCHAR(100),
    product_category VARCHAR(50),
    unit_price DECIMAL(10,2),
    current_stock_level INT
);

CREATE TABLE IF NOT EXISTS raw.customer_details (
    customer_id VARCHAR(20),
    first_name VARCHAR(50),
    email VARCHAR(100),
    loyalty_status VARCHAR(20),
    total_loyalty_points INT,
    last_purchase_date DATE,
    segment_id VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS raw.promotion_details (
    promotion_id VARCHAR(10),
    promotion_name VARCHAR(100),
    start_date DATE,
    end_date DATE,
    discount_percentage DECIMAL(5,2),
    applicable_category VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS raw.loyalty_rules (
    rule_id INT,
    rule_name VARCHAR(100),
    points_per_unit_spend DECIMAL(5,2),
    min_spend_threshold DECIMAL(10,2),
    bonus_points INT
);

CREATE TABLE IF NOT EXISTS raw.store_sales_header (
    transaction_id VARCHAR(30),
    customer_id VARCHAR(20),
    store_id VARCHAR(10),
    transaction_date TIMESTAMP,
    total_amount DECIMAL(10,2)
);

CREATE TABLE IF NOT EXISTS raw.store_sales_line_items (
    line_item_id INT,
    transaction_id VARCHAR(30),
    product_id VARCHAR(20),
    promotion_id VARCHAR(10),
    quantity INT,
    line_item_amount DECIMAL(10,2)
);

-- =========================
-- STAGING TABLES (CLEAN DATA)
-- =========================

CREATE TABLE IF NOT EXISTS staging.store_sales_header (
    transaction_id VARCHAR(30) PRIMARY KEY,
    customer_id VARCHAR(20),
    store_id VARCHAR(10),
    transaction_date TIMESTAMP,
    total_amount DECIMAL(10,2)
);

CREATE TABLE IF NOT EXISTS staging.store_sales_line_items (
    line_item_id INT,
    transaction_id VARCHAR(30),
    product_id VARCHAR(20),
    promotion_id VARCHAR(10),
    quantity INT,
    line_item_amount DECIMAL(10,2)
);

-- =========================
-- QUARANTINE TABLE
-- =========================

CREATE TABLE IF NOT EXISTS staging.quarantine_records (
    source_table VARCHAR(50),
    record_data JSONB,
    error_reason TEXT,
    rejected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
