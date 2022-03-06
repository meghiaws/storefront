FROM postgres:13.6
COPY db_init.sql /docker-entrypoint-initdb.d/