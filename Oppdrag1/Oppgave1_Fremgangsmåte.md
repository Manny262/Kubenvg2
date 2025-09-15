# Fremgangsmåte: 
## 1. Koble til nettverk      
  - Koble klient og server til samme lan
  - Gi server en statisk ip og sett subnet mask til 255.0.0.0.
## 2. Opprette en Webserver med Django
- ### På pcen:
    - Opprette et virtual environment på Pcen (skal lage en requirements.txt fordi virtual enviroment innstallert på en pc, kommer ikke til å fungere på en annen pc.   requirements fil forteller istedenfor serveren hvilke pakker som trengs)
    - lage et nytt prosjekt 
    - opprette en APP 
    - connecte APP til prosjektet (så du kan kjøre applikasjonen)
    - kjøre prosjektet på pcen, for å sjekke at alt fungerer
    - Pushe prosjektet til git 
- ### På server:
    - Klone prosjektet fra Git
    - sette opp et python miljø
    - installere requirements.txt 
    - kjøre migrasjoner
    - Starte django serveren
