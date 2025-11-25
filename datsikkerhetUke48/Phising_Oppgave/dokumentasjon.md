# Phishing-detektiv

## Scenario
- BankID må fornyes en gang i blant. Da får man en mail fra banken, der det står at BankID utløper om ... dager og må derfor fornyes. Jeg tenkte å lage en mail der det står at BankID må fornyes idag, hvis ikke så blir den slettet. 

## Epost: 
1. Avsender: donotreply@sikkerhet.BankID.no
2. Emnefelt: Utløpelsesdato BankID
3. Tekst:  
    Kjære kunde
    En BankID har en Begrenset levetid. Din BankID utløper idag og må derfor fornyes. 
    Bruk vedlagt lenke for å logge deg inn på BankID sin nettside snarest mulig. Din BankID vil da fornyes automatisk.
    Dersom du ikke fornyer din BankID vil den bli slettet idag. 

    Vennligst vær oppmerksom på at dersom din BankID blir slettet, medfører dette at BankID må fysisk bestilles på nytt i Stø AS sitt lokale i Stavanger.    
4. Bunntekst: 
    {BankID logo}
    Stø AS
    Orgnr. 937 621 929

## Teknikker: 
### Psykologiske triks: 
- Jeg brukte hastverk og frykt, for å få "brukeren" til å haste seg med å fornye BankID'en sin, fordi hen kan risikere å miste tilgang til f.eks nettbank og Helsenorge.  
### Visuelle Elementer: 
- Jeg mener at designet er troverdig, fordi jeg brukte samme skrift og størrelse som banken min sendte til meg, og jeg formulerte meg på samme måte. Jeg la også med Stø AS (eier av BankID) sitt organisasjonsnummer i bunnteksten, samt BankID sin logo. 
### Røde Flagg: 
- Mailen inneholder feil Organisasjonsnummer for Stø AS
- BankID og banker pleier ikke å sende ut mailer med en lenke til innloggingsiden. Man kan oppdage dette ved å se tilbake på gamle meldinger fra Banken. 
- I mailen så står det at man må dra til Stø sitt lokale i Stavanger hvis man ikke fornyer BankID idag. Jeg ville ha sjekket om Stø hadde lokale i Stavanger (noe som de ikke har) før jeg ville ha trykket på linken.

## Hva ville jeg ha gjort i hvis jeg fikk denne mailen?
1. Sjekke hvis jeg har tidligere mail fra avsenderen, og hvordan de så ut (font, linjeavstand, størrelse, osv).
2. Hvor troverdig er avsender? Jeg ville ha søkt på organisasjonsnummeret og sjekke om Stø er et registrert AS.
3. Istedenfor å trykke på lenken, så ville jeg heller gått inn på BankID sin nettside, og logget meg inn via den. 