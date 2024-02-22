/*
    Title: wilson_db_init.sql
    Author: Jacob Ambrose / John Martino, Jackie Scott / Marshall Huckins
    Date: 02/21/2024
    Description: Willson Financial database initialization script.
*/

-- drop database user if exists 
DROP USER IF EXISTS 'wilson_user'@'localhost';


-- create movies_user and grant them all privileges to the movies database 
CREATE USER 'wilson_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'financial';

-- grant all privileges to the movies database to user movies_user on localhost 
GRANT ALL PRIVILEGES ON movies.* TO 'wilson_user'@'localhost';


-- drop tables if they are present




-- create the studio table 



-- create the genre table 



-- create the film table and set the foreign key



-- insert studio records

	
-- insert genre records


-- insert movie records 
