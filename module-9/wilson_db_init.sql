/*
    Title: wilson_db_init.sql
    Author: Jacob Ambrose, Marshall Huckins, John Martino, Jackie Scott
    Date: 02/24/2024
    Description: assets database initialization script
*/

-- drop database user if exists 
DROP USER IF EXISTS 'wilson_user'@'localhost';


-- create movies_user and grant them all privileges to the movies database 
CREATE USER 'wilson_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'financial';

-- grant all privileges to the movies database to user movies_user on localhost 
GRANT ALL PRIVILEGES ON bravo.* TO 'wilson_user'@'localhost';


-- drop tables if they are present
DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS assets;




-- create the transaction table 
CREATE TABLE transactions (
    transaction_id     INT             NOT NULL        AUTO_INCREMENT,
    transaction_date   DATE     NOT NULL,
    invoice_number   VARCHAR(75)     NOT NULL,
     
    PRIMARY KEY(transaction_id)
); 

-- create the asset table 
CREATE TABLE assets (
    asset_id     INT             NOT NULL        AUTO_INCREMENT,
    asset_type   VARCHAR(75)     NOT NULL,
    asset_value   DECIMAL(10,2)     NOT NULL,
     
    PRIMARY KEY(asset_id)
); 
-- create the client table and set the foreign key
    CREATE TABLE clients (
        client_id   INT             NOT NULL        AUTO_INCREMENT,
        client_name  VARCHAR(75)     NOT NULL,
        client_address VARCHAR(75) NOT NULL,
        client_phone VARCHAR(15) NOT NULL,
        client_email VARCHAR(75) NOT NULL,
        client_startDate   DATE     NOT NULL,
        
        PRIMARY KEY(client_id),

        -- CONSTRAINT fk_transaction
        -- FOREIGN KEY(transaction_id)
        --     REFERENCES transaction(transaction_id),
            
        -- CONSTRAINT fk_asset
        -- FOREIGN KEY(asset_id)
        --     REFERENCES asset(asset_id)	
    );


-- insert transaction records
INSERT INTO transactions(transaction_date, invoice_number)
    VALUES('2020-11-26', 'INV0001');
INSERT INTO transactions(transaction_date, invoice_number)
    VALUES('2020-11-29', 'INV0002');
INSERT INTO transactions(transaction_date, invoice_number)
    VALUES('2022-05-06', 'INV0003');
INSERT INTO transactions(transaction_date, invoice_number)
    VALUES('2023-02-15', 'INV0004');
INSERT INTO transactions(transaction_date, invoice_number)
    VALUES('2021-08-15', 'INV0005');
INSERT INTO transactions(transaction_date, invoice_number)
    VALUES('2022-01-25', 'INV0006');
INSERT INTO transactions(transaction_date, invoice_number)
    VALUES('2021-03-01', 'INV0007');
INSERT INTO transactions(transaction_date, invoice_number)
    VALUES('2023-06-02', 'INV0008');
INSERT INTO transactions(transaction_date, invoice_number)
    VALUES('2022-05-01', 'INV0009');
INSERT INTO transactions(transaction_date, invoice_number)
    VALUES('2024-01-18', 'INV0010');
INSERT INTO transactions(transaction_date, invoice_number)
    VALUES('2024-02-01', 'INV0011');
INSERT INTO transactions(transaction_date, invoice_number)
    VALUES('2023-05-18', 'INV0012');


	
-- insert asset records
INSERT INTO assets(asset_type, asset_value)
    VALUES('MONEY', '100000');
INSERT INTO assets(asset_type, asset_value)
    VALUES('LAND', '800000');
INSERT INTO assets(asset_type, asset_value)
    VALUES('LIVESTOCK', '50000');
INSERT INTO assets(asset_type, asset_value)
    VALUES('LAND', '427000');
INSERT INTO assets(asset_type, asset_value)
    VALUES('EQUIPMENT', '740000');
INSERT INTO assets(asset_type, asset_value)
    VALUES('VEHICLES', '80000');
INSERT INTO assets(asset_type, asset_value)
    VALUES('LAND', '500000');
INSERT INTO assets(asset_type, asset_value)
    VALUES('VEHICLES', '50000');
INSERT INTO assets(asset_type, asset_value)
    VALUES('MONEY', '75000');
INSERT INTO assets(asset_type, asset_value)
    VALUES('EQUIPMENT', '25000');
INSERT INTO assets(asset_type, asset_value)
    VALUES('LAND', '650000');


-- insert movie records 
	INSERT INTO clients (client_name, client_address, client_phone, client_email, client_startDate) 
    VALUES('JOHN DOE', '1110 SYLVAN', '805252722', 'jambrose@gmail.com', '2022-04-08' );
