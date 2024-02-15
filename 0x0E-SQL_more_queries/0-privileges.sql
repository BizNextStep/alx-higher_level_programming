-- This script lists all privileges of the MySQL users user_0d_1 and user_0d_2 on the server.

-- List privileges for user_0d_1
SELECT * FROM mysql.user WHERE user = 'user_0d_1';

-- List privileges for user_0d_2
SELECT * FROM mysql.user WHERE user = 'user_0d_2';
