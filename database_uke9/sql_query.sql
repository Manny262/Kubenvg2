CREATE EXTENSION IF NOT EXISTS citext;
-- Drop table Category Cascade;
-- Drop table Inventory Cascade;
-- Drop table Item Cascade;
-- Drop table Warehouse Cascade;
-- Drop table Contact_person Cascade;
-- Drop table Supplier Cascade;


create table Category(
category_id SERIAL PRIMARY KEY,
category_name varchar(100),
description TEXT
);

Create table Warehouse(
warehouse_id SERIAL PRIMARY KEY,
warehouse_name VARCHAR(100),
adress VARCHAR(200),
city VARCHAR(100)
);
create table Contact_person(
contact_person_id SERIAL PRIMARY KEY,
contact_name varchar(100),
email CITEXT UNIQUE,
phone TEXT UNIQUE
-- supplier_id INTEGER REFERENCES Supplier(supplier_id)
);

create table Supplier(
supplier_id SERIAL PRIMARY KEY,
supplier_name varchar(100),
phone TEXT UNIQUE,
email CITEXT NOT NULL UNIQUE 
-- contact_person_id INTEGER REFERENCES Contact_person(contact_person_id),
);

Create table Item(
item_id SERIAL PRIMARY KEY,
item_name VARCHAR(100),
price DECIMAL(10,2),
category_id INTEGER REFERENCES Category(category_id)
-- supplier_id INTEGER REFERENCES Supplier(supplier_id),
);

create table Inventory(
inventory_id SERIAL PRIMARY KEY,
item_id INTEGER REFERENCES Item(item_id),
warehouse_id INTEGER REFERENCES Warehouse(warehouse_id),
number_of_items INTEGER 
);





-- SELECT  i.item_name, n.number_of_items,  i.price, W.warehouse_name,  c.category_name, s.supplier_name,n.inventory_id, n.item_id, i.supplier_id, n.warehouse_id
--                                    FROM Inventory n
--                                     INNER JOIN Warehouse W USING(warehouse_id)
--                                     INNER JOIN Item i USING(item_id)
--                                     INNER JOIN Supplier s USING(supplier_id)
--                                     LEFT JOIN Category c USING(category_id)



ALTER TABLE Contact_person ADD COLUMN supplier_id INTEGER REFERENCES Supplier(supplier_id);
ALTER TABLE Item ADD COLUMN supplier_id INTEGER REFERENCES Supplier(supplier_id);
Alter TABLE Supplier ADD COLUMN contact_person_id INTEGER REFERENCES Contact_person(contact_person_id);
-- ALTER TABLE Item Drop COLUMN warehouse_id;

-- ALTER TABLE Contact_person ADD COLUMN contact_name varchar(100);

select e.item_id, e.item_name, W.warehouse_name 
from Item e
left Join Warehouse W
on e.warehouse_id = W.warehouse_id
