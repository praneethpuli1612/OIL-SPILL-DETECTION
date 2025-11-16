DROP DATABASE IF EXISTS rainfall;
CREATE DATABASE rainfall;
USE rainfall;

CREATE TABLE user2 (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(225),
    email VARCHAR(225),
    password VARCHAR(225)
);
