schema_prompt = """CREATE TABLE IF NOT EXISTS transactions (
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
-- Using valid SQLite, answer the following questions for the tables provided above.
"""

concert_schema ="""CREATE TABLE stadium (
    stadium_id number,
    location text,
    name text,
    capacity number,
    highest number,
    lowest number,
    average number
)

CREATE TABLE singer (
    singer_id number,
    name text,
    country text,
    song_name text,
    song_release_year text,
    age number,
    is_male others
)

CREATE TABLE concert (
    concert_id number,
    concert_name text,
    theme text,
    stadium_id text,
    year text
)

CREATE TABLE singer_in_concert (
    concert_id number,
    singer_id text
)
-- Using valid SQLite, answer the following questions for the tables provided above.
"""