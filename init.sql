CREATE TABLE IF NOT EXISTS transactions (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    gender VARCHAR(10) NULL,
    birthdate DATE NOT NULL,
    transaction_amount DECIMAL(10, 2) NOT NULL,
    transaction_date DATE NOT NULL,
    merchant_name VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL
);
COPY transactions FROM '/data/sample_dataset.csv' DELIMITER ',' CSV HEADER;
