    -- Test Warehouses (Varehus)
    INSERT INTO Warehouse (warehouse_name, adress, city) VALUES
    ('Oslo Lager', 'Storgata 42', 'Oslo'),
    ('Bergen Lager', 'Vågsalmenningen 15', 'Bergen'),
    ('Stavanger Lager', 'Nygata 8', 'Stavanger'),
    ('Trondheim Lager', 'Olav Tryggvasons gate 10', 'Trondheim');

    -- Test Items (Varer)
    INSERT INTO Item (warehouse_id, item_name, price, category) VALUES
    -- Oslo Lager items
    (1, 'Laptop Dell XPS 13', 12990.00, 'Elektronikk'),
    (1, 'Trådløs Mus Logitech', 349.00, 'Tilbehør'),
    (1, 'USB-C Kabel 2m', 199.00, 'Tilbehør'),
    (1, 'Monitor LG 27"', 3490.00, 'Elektronikk'),

    -- Bergen Lager items
    (2, 'Tastatur Mekanisk RGB', 899.00, 'Tilbehør'),
    (2, 'Webkamera HD', 599.00, 'Elektronikk'),
    (2, 'Skjermlys BenQ e-Reading', 1299.00, 'Elektronikk'),
    (2, 'Headset Gaming Corsair', 1499.00, 'Elektronikk'),

    -- Stavanger Lager items
    (3, 'Ekstern Harddisk 2TB', 799.00, 'Lagring'),
    (3, 'SSD 500GB NVMe', 499.00, 'Lagring'),
    (3, 'Minnekort SD 128GB', 249.00, 'Lagring'),

    -- Trondheim Lager items
    (4, 'Strømforsyning 650W', 699.00, 'Komponenter'),
    (4, 'Grafikkort RTX 3060', 4990.00, 'Komponenter'),
    (4, 'Prosessor Intel i7', 3990.00, 'Komponenter');
