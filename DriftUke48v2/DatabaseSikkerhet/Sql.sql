Create table pizzaer(
 id Serial primary key,
 navn varchar(100),
 pris decimal(5,2)
);
Create User testBrukerSikkerhet with password '12345';
Grant connect on database data_sikkerhet_uke48 to testbrukersikkerhet;
Grant Select on brukere to testBrukerSikkerhet;


Insert into pizzaer (navn, pris) Values
('Margherita', 119.00),
('Pepperoni', 135.00),
('Vegetar', 125.00),
('Kebabpizza', 145.00);

select * from pizzaer

Create table brukere(
 id Serial primary key,
 brukernavn varchar(100),
 passord Varchar(100)
);
Insert Into brukere (brukernavn, passord) values
('admin', 1234),
('bruker1', 'hemmelig123');