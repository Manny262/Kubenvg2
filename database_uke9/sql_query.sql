Create table Warehouse(
warehouse_id SERIAL PRIMARY KEY,
warehouse_name VARCHAR(100),
adress VARCHAR(200),
city VARCHAR(100)
);

Create table Item(
item_id SERIAL PRIMARY KEY,
warehouse_id INTEGER REFERENCES Warehouse(warehouse_id),
item_name VARCHAR(100),
price DECIMAL(10,2),
category VARCHAR(50)
);




