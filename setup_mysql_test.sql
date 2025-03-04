--create a database called hbnb_test_db in MySQL server
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
--creates a new user hbnb_test 
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
--Grants permissions for user hbnb_test
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
