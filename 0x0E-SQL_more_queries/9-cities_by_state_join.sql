-- This script lists all cities contained in the database hbtn_0d_usa
-- along with their corresponding state names.

-- Use database hbtn_0d_usa
USE hbtn_0d_usa;

-- List all cities with their corresponding state names
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
