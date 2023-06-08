-- Create a database for testing purposes
CREATE DATABASE IF NOT EXISTS dev_caseshare;
CREATE USER IF NOT EXISTS 'caseadmin'@'localhost' IDENTIFIED BY 'caseadminpwd';
GRANT ALL ON dev_caseshare.* TO 'caseadmin'@'localhost';
SHOW GRANTS FOR 'caseadmin'@'localhost';
