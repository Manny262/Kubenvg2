Use treningsenter;
Create user 'trenings-admin'@'localhost' IDENTIFIED by 'passord';
Grant all PRIVILEGES on treningsenter.* to 'trenings-admin'@'localhost';
Flush PRIVILEGES

 create table Medlem(
        ID int primary key auto_increment not null,
        FORNAVN varchar(30) not null,
        ETTERNAVN varchar(40) not null,
        EMAIL varchar(40) unique not null,
        TELEFON varchar(8) unique not null,
        MEDLEMSKAP_START timestamp default current_timestamp
        );

        create table Instruktør(
            ID int primary key auto_increment not null,
            FORNAVN varchar(30) not null,
            ETTERNAVN varchar(40) not null,
            SPESIALITET varchar(100)
        );

        create table Økt(
            ID int primary key auto_increment not null,
            ØKT_NAVN varchar(50) not null,
            TIDSPUNKT timestamp not null, 
            INSTRUKTØR_ID int not null,
            MAKS_DELTAKERE int not null,
            foreign key (INSTRUKTØR_ID) references Instruktør(ID)
        );

        create table Påmelding(
           ID int primary key auto_increment not null,
           MEDLEM_ID int,
           ØKT_ID int, 
           foreign key (MEDLEM_ID) references Medlem(ID),
           foreign key (ØKT_ID) references Økt(ID),
           PÅMELDINGSDATO timestamp default current_timestamp 
        );

    
        INSERT INTO Medlem (FORNAVN, ETTERNAVN, EMAIL, TELEFON) VALUES
        ('Anna', 'Hansen', 'anna.hansen@email.com', '12345678'),
        ('Bjørn', 'Olsen', 'bjorn.olsen@email.com', '23456789'),
        ('Clara', 'Nilsen', 'clara.nilsen@email.com', '34567890'),
        ('David', 'Johansen', 'david.johansen@email.com', '45678901'),
        ('Eva', 'Berg', 'eva.berg@email.com', '56789012');


        INSERT INTO Instruktør (FORNAVN, ETTERNAVN, SPESIALITET) VALUES
        ('Siri', 'Larsen', 'Spinning'),
        ('Morten', 'Solberg', 'Yoga'),
        ('Kari', 'Andersen', 'Styrke');


        INSERT INTO Økt (ØKT_NAVN, TIDSPUNKT, INSTRUKTØR_ID, MAKS_DELTAKERE) VALUES
        ('Morgenspinning', '2024-06-10 07:00:00', 1, 15),
        ('Kveldsyoga', '2024-06-10 18:00:00', 2, 12),
        ('Styrke 1', '2024-06-11 17:00:00', 3, 10),
        ('Spinning Ekstra', '2024-06-12 08:00:00', 1, 15),
        ('Yoga Rolig', '2024-06-12 19:00:00', 2, 12),
        ('Styrke 2', '2024-06-13 17:00:00', 3, 10);

     
        INSERT INTO Påmelding (MEDLEM_ID, ØKT_ID) VALUES
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 2),
        (5, 3),
        (1, 4),
        (2, 4),
        (3, 5),
        (4, 6),
        (5, 6);

        select * from Økt where INSTRUKTØR_ID = 2
        
        select count(*) from Påmelding where ØKT_ID = 1

        select MEDLEM_ID from Påmelding where ØKT_ID = 4

Create user 'resepsjonist'@'localhost' IDENTIFIED by 'RE';
Grant select on treningsenter.* to 'resepsjonist'@'localhost';
Flush PRIVILEGES;

mysql -u resepsjonist -p 
select MEDLEM_ID from Påmelding where ØKT_ID = 3;     
insert into  INSERT INTO Påmelding (MEDLEM_ID, ØKT_ID) VALUES(1, 1);