DROP USER IF EXISTS 'userPro'@'localhost';
CREATE USER 'userPro'@'localhost' IDENTIFIED BY 'pass';
GRANT SELECT, UPDATE, INSERT, DELETE, EXECUTE ON Prorest.* TO 'userPro'@'localhost';