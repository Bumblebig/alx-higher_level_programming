-- creates database
CREATE DATABASE IF NOT EXISTS htbn_0d_usa;
-- switch database
USE hbtn_0d_usa;
-- creates table with a column with auto increment as a primary key
CREATE TABLE IF NOT EXISTS states (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(256) NOT NULL,
  UNIQUE(id)
);
