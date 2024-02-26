CREATE TABLE IF NOT EXISTS transactions
(
    customer_id        SERIAL PRIMARY KEY,
    name               VARCHAR(255)   NOT NULL,
    surname            VARCHAR(255)   NOT NULL,
    gender             VARCHAR(10)    NULL,
    birthdate          DATE           NOT NULL,
    transaction_amount DECIMAL(10, 2) NOT NULL,
    transaction_date   DATE           NOT NULL,
    merchant_name      VARCHAR(255)   NOT NULL,
    category           VARCHAR(255)   NOT NULL
);
COPY transactions FROM '/data/sample_dataset.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE IF NOT EXISTS stadium
(
    stadium_id int,
    location   text,
    name       text,
    capacity   int,
    highest    int,
    lowest     int,
    average    int
);
COPY stadium FROM '/data/stadium_with_fk.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE IF NOT EXISTS singer
(
    singer_id         int,
    name              text,
    country           text,
    song_name         text,
    song_release_year text,
    age               int,
    is_male           boolean
);
COPY singer FROM '/data/singer_with_fk.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE IF NOT EXISTS concert
(
    concert_id   int,
    concert_name text,
    theme        text,
    stadium_id   text,
    year         text
);
COPY concert FROM '/data/concert_with_fk.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE singer_in_concert
(
    concert_id int,
    singer_id  text
);
COPY singer_in_concert FROM '/data/singer_in_concert_with_fk.csv' DELIMITER ',' CSV HEADER;
