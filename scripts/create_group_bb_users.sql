-- usage: 
--  psql blue_bite -f [this file]
--      otherwise, "no relation tag" error on grant all privileges on table

DROP ROLE IF EXISTS bb_users;

CREATE ROLE bb_users;

GRANT CONNECT ON DATABASE blue_bite TO bb_users;

GRANT USAGE ON SCHEMA public TO bb_users;

GRANT ALL PRIVILEGES ON DATABASE blue_bite TO bb_users;

GRANT ALL PRIVILEGES ON TABLE tag TO bb_users;
