CREATE DATABASE bump_it_db;

CREATE USER main_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE bump_it_db TO main_admin;

ALTER DATABASE bump_it_db OWNER TO main_admin;