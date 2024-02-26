# Use the official PostgreSQL image from Docker Hub
FROM postgres:latest

# Set the environment variables\
COPY .env .env
RUN sh .env

ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword
ENV POSTGRES_DB=mydatabase


# Copy the SQL script to initialize the database
COPY init.sql /docker-entrypoint-initdb.d/
COPY data /data