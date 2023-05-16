-- Changes property of database in server
ALTER DATABASE hbtn_0c_0
    CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Changes properties of a table in database
USE hbtn_0c_0;
ALTER TABLE first_table
    CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
