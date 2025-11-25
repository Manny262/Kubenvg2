
- Den usikre spørringen bruker f-string for å direkte plassere inn brukerens input, noe som gjør at input'en blir en del av selve sql-koden. 
- Den sikre spørringen bruker parameter for å unngå at potensielle hackere kan bruke spesial tegn som ' OR '1'='1. brukerens input blir da behandlet som data istedenfor kode.  