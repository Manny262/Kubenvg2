-- Testcases for tabellene i sql_query.sql
-- Kjor hver blokk separat ved behov. Kommentarer er pa norsk.

-- 1) Warehouse: gyldige innsettinger
INSERT INTO Warehouse (warehouse_name, adress, city) VALUES
('Test Lager A', 'Testgata 1', 'Oslo'),
('Test Lager B', 'Testgata 2', 'Bergen');

-- 2) Category: gyldige innsettinger
INSERT INTO Category (category_name, description) VALUES
('Elektronikk', 'Elektroniske produkter'),
('Tilbehor', 'Kabler, mus, tastatur og lignende');

-- 3) Item: gyldig innsetting med kobling til Warehouse og Category
INSERT INTO Item (warehouse_id, item_name, price, category_id) VALUES
(1, 'Test Laptop', 9999.00, 1),
(2, 'Test Mus', 199.00, 2);

-- 4) Inventory: gyldig innsetting
INSERT INTO Inventory (item_id, warehouse_id, number_of_items) VALUES
(1, 1, 10),
(2, 2, 25);

-- 5) Contact_person: gyldige innsettinger (unik epost og telefon)
INSERT INTO Contact_person (email, phone) VALUES
('kontaktA@example.com', '11111111'),
('kontaktB@example.com', '22222222');

-- 6) Supplier: gyldig innsetting med kobling til Contact_person
INSERT INTO Supplier (supplier_name, contact_person_id, phone, email) VALUES
('Leverandor A', 1, '33333333', 'leverandorA@example.com'),
('Leverandor B', 2, '44444444', 'leverandorB@example.com');

-- 7) Contact_person: oppdatering av supplier_id (FK referanse)
UPDATE Contact_person SET supplier_id = 1 WHERE contact_person_id = 1;
UPDATE Contact_person SET supplier_id = 2 WHERE contact_person_id = 2;

-- 8) Negativ test: duplikat epost i Contact_person (skal feile)
-- INSERT INTO Contact_person (email, phone) VALUES
-- ('kontaktA@example.com', '55555555');

-- 9) Negativ test: ugyldig warehouse_id i Item (skal feile)
-- INSERT INTO Item (warehouse_id, item_name, price, category_id) VALUES
-- (999, 'Ugyldig Lager', 10.00, 1);

-- 10) Negativ test: ugyldig category_id i Item (skal feile)
-- INSERT INTO Item (warehouse_id, item_name, price, category_id) VALUES
-- (1, 'Ugyldig Kategori', 10.00, 999);

-- 11) Negativ test: duplikat epost i Supplier (skal feile)
-- INSERT INTO Supplier (supplier_name, contact_person_id, phone, email) VALUES
-- ('Leverandor C', 1, '66666666', 'leverandorA@example.com');

-- 12) Verifikasjon: enkel sjekk av relasjoner
SELECT i.item_id, i.item_name, w.warehouse_name, c.category_name
FROM Item i
JOIN Warehouse w ON i.warehouse_id = w.warehouse_id
JOIN Category c ON i.category_id = c.category_id;

SELECT s.supplier_id, s.supplier_name, cp.email, cp.phone
FROM Supplier s
JOIN Contact_person cp ON s.contact_person_id = cp.contact_person_id;
