-- 5. Unique ID

-- Create the unique_id table if it does not exist
CREATE TABLE IF NOT EXISTS unique_id (
id INT DEFAULT 1 UNIQUE,
name VARCHAR(256)
);

