## Ikke startet:
- Comboboks på Tjeneste??
- Filter på sak til sak
- saksansvarlig navn

- vedlegg: dato endret og opprettet, siste mann som endret. 
## jobber med:

- styling

## ferdig:


- Forms knapp for å sumbite.

- sak til sak.
    - Viktigst forside og side2:  
        Tittel, Frist-forvaltningsak (hvis det er forvaltningsak), beskrivelse, sakstype, status, fremdriftsansvarlig, 
    - lagre tabell som en variabel istedenfor data source
    - forms vil ikke vise Dataitem i preview (muligens fordi det er record og ikke table?? )
    - dato på kommentarer
    - filter: 
        -forvaltningsområde
        -nyeste til eldste
        -Status
    - Kommentarer
    - Tabellkolonner: 
        -Sakstype
        -attachments 


# notater:
- kommentarer til liste


# power fx

Test auto-generate: 

/
Filter(
    SamhandlingTable,
    (FilterSaksType.Selected.Value = "alle" || IsBlank(FilterSaksType) || Sakstype.Value = FilterSaksType.Selected.Value),
    (FilterRiskLevel.Selected.Value = "alle" || IsBlank(FilterRiskLevel) || RiskLevel.Value = FilterRiskLevel.Selected.Value),
    (FilterTjeneste.Selected.Value = "alle" || IsBlank(FilterTjeneste) || Tjeneste.Value = FilterTjeneste.Selected.Value),
    (CountRows(ComboForvaltning.SelectedItems) = 0 || CountRows(Filter(ComboForvaltning.SelectedItems, ThisRecord.Value in Forvaltningsområde)) > 0),
    (FilterStatus_1.Selected.Value = "alle" || IsBlank(FilterStatus_1) || Status.Value = FilterStatus_1.Selected.Value),
    (CheckRelease = false || Releasedato = FilterReleaseDato.SelectedDate),
    (CheckFrist = false || Frist_Forvaltningssak = FilterFristForvaltningsak.SelectedDate)
)

Title: "Test Case " & Text(ThisRecord.Value, "000"),
Beskrivelse: "random",
Tjeneste: 
    Switch(
        Applikasjoner (Apple)
        Applikasjoner (Windows)
        ASM (Apple School Manager)
        Autentiseringstjenester
        BNS25-26
        Brukerimport
        Driftsportalen
        Eksamensløsning
        Entra ID
        Exchange
        Forvaltningsmøte Drift
        Generell tjenesteoppfølging
        Infrastruktur og plattform drift
        Integrasjoner
        Intune
        iOS, tvOS, MacOS
        Jamf School
        Klassestyring
        LSI
        M365 for utdanning
        Nettfiltrering
        Nettverk
        PC klienter
        Portalen
        Servicedesk
        SharePoint
        Sikkerhet
        Skolekode
        Skolemelding
        Skolens nettsider
        Skolenyhet
        SOC-tjenesten
        Teams
        Utskriftstjenester
        Vigo-Bas/(MIM)       
    ),
Forvaltningsområde:
    Switch(
       Autentisering
       Digitale enheter (Apple)
       Digitale enheter (Windows) og utskrift
       Drift
       Internettstyring
       Microsoft 365
       Nettsider og skolehjem-kommunikasjon
       Sikkerhet
       Tilgangsstyring og integrasjoner
       

    )
Frist_forvaltningssak: Today() + RandBetween(1, 60),
Sakstype:
Switch(
RandBetween(1,3),
1, "Forvaltningssak",
2, "Ordinær endring",
3, "Enkel feilrettning"
),
Fremdriftsansvarlig:
If(
RandBetween(1,2) = 1,
"CGI",
"UDE"
),
Risikonivå:
Switch(
RandBetween(1,3),
1, "Lav",
2, "Medium",
3, "Høy"
)
}
)
);
Notify("100 test cases opprettet!", NotificationType.Success);



json-schema: 
{
    "body": [
        {
            "Title": "Test1",
            "Beskrivelse": "rjqwjoeqji2ojq",
            "Tjeneste": null,
            "Status": "Estimeres",
            "Frist_Forvaltningssak": "2025-10-22",
            "Sakstype": "Forvaltningssak",
            "RiskLevel": "lav",
            "Fremdriftsansvarling": "UDE",
            "Saksansvarlig(UDE)": {
                "@odata.type": "#Microsoft.Azure.Connectors.SharePoint.SPListExpandedUser",
                "Claims": "i:0#.f|membership|sindre0306@osloskolen.no",
                "DisplayName": "Sindre Ohm-Hagen",
                "Email": "sindre.ohm-hagen@osloskolen.no",
                "Picture": "https://udeoslokommuneno.sharepoint.com/sites/UDA-T-IKT-SandkassetilPP-utviklere/_layouts/15/UserPhoto.aspx?Size=L&AccountName=sindre.ohm-hagen@osloskolen.no",
                "Department": "UDA-IKT Avdeling",
                "JobTitle": null
            },
            "Releasedato": "2025-10-20",
            "Forvaltingsområde": null
        },
        {
            "Title": "Test2 ",
            "Beskrivelse": "",
            "Tjeneste": "Office365",
            "Status": "Estimeres",
            "Frist_Forvaltningssak": "2025-10-22",
            "Sakstype": "Forvaltningssak",
            "RiskLevel": "medium",
            "Fremdriftsansvarling": "UDE",
            "Saksansvarlig(UDE)": null,
            "Releasedato": "2025-10-21",
            "Forvaltingsområde": null
        }
    ]
}

Filter: 
Filter(
    Manelin_oppgave_samhandling,
    (FilterSaksType.Selected.Value = "alle" || IsBlank(FilterSaksType) || Sakstype.Value = FilterSaksType.Selected.Value),
    (FilterRiskLevel.Selected.Value = "alle" || IsBlank(FilterRiskLevel) || RiskLevel.Value = FilterRiskLevel.Selected.Value),
    (FilterTjeneste.Selected.Value = "alle" || IsBlank(FilterTjeneste) || Tjeneste.Value = FilterTjeneste.Selected.Value),
    (CheckRelease=false || Releasedato = FilterReleaseDato.SelectedDate),
    (CheckFrist=false || Frist_Forvaltningssak = FilterFristForvaltningsak.SelectedDate)

)

URI: 
_api/web/lists/(guid'{5246e74c-759f-406a-b12e-5f6a64c7ff39}')/items(3)/comments


http output: 
    "body": {
        "value": [
            {
                "author": {
                    "directoryObjectId": null,
                    "email": "mawia031@osloskolen.no",
                    "expiration": null,
                    "id": 37,
                    "isActive": true,
                    "isExternal": false,
                    "jobTitle": null,
                    "loginName": "i:0#.f|membership|mawia031@osloskolen.no",
                    "name": "Manelin Haaland Windwood",
                    "principalType": 1,
                    "userId": null,
                    "userPrincipalName": null
                },
                "createdDate": "2025-10-29T08:10:14.217Z",
                "id": "2",
                "isLikedByUser": false,
                "isReply": false,
                "itemId": 2,
                "likeCount": 0,
                "listId": "5246e74c-759f-406a-b12e-5f6a64c7ff39",
                "mentions": [],
                "modifiedDate": null,
                "parentId": "0",
                "replyCount": 0,
                "text": "esdksahjkwahdsahkldsa"
            }
        ]

    test: 
    {
    "variables": [
        {
            "name": "CommentsArray",
            "type": "Array",
            "value": [
                {
                    "email": "mawia031@osloskolen.no",
                    "Name": "Manelin Haaland Windwood",
                    "Text": "sasadsadxc"
                },
                {
                    "email": "mawia031@osloskolen.no",
                    "Name": "Manelin Haaland Windwood",
                    "Text": "esdksahjkwahdsahkldsa"
                }
            ]
        }
    ]
}



adlsøasld: {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "email": {
                "type": "string"
            },
            "Name": {
                "type": "string"
            },
            "Text": {
                "type": "string"
            }, 
           
            
        },
        "required": [
            "email",
            "Name",
            "Text"
        ]
    }
}