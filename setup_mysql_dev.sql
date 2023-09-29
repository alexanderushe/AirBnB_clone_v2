--creates a database hbnb_dev_db in MYSQL
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
--creates new user hbnb_dev
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
--grants permissions for user hbnb_dev
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
--flush privileges to apply changes
FLUSH PRIVILEGES;
