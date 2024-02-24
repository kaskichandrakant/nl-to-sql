# Ask Anything About Your Database

Created with llama 2's fine-tuned pretrained model nsql-350M

``Running with Python 3.11.0 and pip 24.0``

## Starting sample db

```shell
# source .env with POSTGRES_USER,POSTGRES_PASSWORD,POSTGRES_DB
 docker build -t mypostgres . 
 docker run -p 5433:5432 mypostgres
```

## Injecting data in sample db

```postgresql
--  Run following script in psql console
COPY transactions FROM '/data/sample_dataset.csv' DELIMITER ',' CSV HEADER;
```

## Starting the application

### installing dependencies

```
virtualenv -p /usr/bin/python3 venv
source ./venv/bin/activate  
pip install -r requirements.txt 
```

```shell
streamlit run main.py     
```

