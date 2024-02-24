import os

import psycopg2

# Connect to the PostgreSQL database
global conn


def connect():
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    database = os.getenv("POSTGRES_DB")
    conn = psycopg2.connect(
        host="localhost",
        port="5433",
        database=database,
        user=user,
        password=password
    )
    return conn

# Create a cursor object
# conn = connect()
# cur = conn.cursor()

# Execute a SQL query
# cur.execute("COPY transactions FROM '/data/sample_dataset.csv' DELIMITER ',' CSV HEADER;")

# Commit the transaction
# conn.commit()

# Close the cursor and connection
# cur.close()
# conn.close()
