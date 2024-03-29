-- This script creates the table unique_id on the MySQL server.

-- Create table unique_id if not exists
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256) NOT NULL
);
