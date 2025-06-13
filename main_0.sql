-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create user if not exists
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant privileges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Use the database
USE hbnb_dev_db;

-- Drop the table if exists (clean start)
DROP TABLE IF EXISTS states;

-- Create the states table
CREATE TABLE states (
    id VARCHAR(60) NOT NULL PRIMARY KEY,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    name VARCHAR(128) NOT NULL
);

-- Insert 5 example states
INSERT INTO states (id, created_at, updated_at, name) VALUES
('421a55f4-7d82-47d9-b54c-a76916479545', NOW(), NOW(), 'Alabama'),
('421a55f4-7d82-47d9-b54c-a76916479546', NOW(), NOW(), 'Arizona'),
('421a55f4-7d82-47d9-b54c-a76916479547', NOW(), NOW(), 'California'),
('421a55f4-7d82-47d9-b54c-a76916479548', NOW(), NOW(), 'Colorado'),
('421a55f4-7d82-47d9-b54c-a76916479549', NOW(), NOW(), 'Florida');
