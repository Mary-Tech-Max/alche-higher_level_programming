-- 6. States table

-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create the states table if it does not exist
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
name VARCHAR(256) NOT NULL
);

