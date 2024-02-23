schema_prompt = """CREATE TABLE stadium (
    stadium_id number,
    location text,
    name text,
    capacity number,
    highest number,
    lowest number,
    average number
)

CREATE TABLE singer (
    singer_id number,xz
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