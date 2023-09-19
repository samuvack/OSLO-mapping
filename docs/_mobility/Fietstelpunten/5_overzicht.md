---
layout: default
parent: Fietstelpunten
title: Overview
nav_order: 5
---


# Verkeersmeting type transportmiddel


```json
"type": "FIETSERS",
"aantal": 0
```

```json
{
  "@context": [
 "https://data.vlaanderen.be/doc/applicatieprofiel/verkeersmetingen/ontwerpstandaard/2023-03-14/context/Verkeersmetingen-ap.jsonld",
 "cl-vrt": "https://data.vlaanderen.be/doc/concept/VkmVoertuigTypes/",
 "cl-vkt": "https://data.vlaanderen.be/doc/concept/VkmVerkeersKenmerkType/",
],

   "@graph": [
    {
      "@id": "_:vrm001",
      "@type": "Verkeersmeting",
      "Verkeersmeting.geobserveerdKenmerk": {
        "@type": "Verkeerskenmerk",
        "Verkeerskenmerk.type": "cl-vkt:aantal",
        "Verkeerskenmerk.voertuigType": "cl-vrt:fiets"
      },
      "Verkeersmeting.resultaat": 60,
      "Verkeersmeting.uitgevoerdDoor": "_:mti001",
      "Verkeersmeting.geobserveerdObject": "_:mpt001",
      "Verkeersmeting.fenomeenTijd": ":_fenomtime001"
    }
   ]

```





# Verkeersmeting.fenomeenTijd

De bron data geeft de tijdperiode met de velden `van` en `tot`:

```json
"van":"2023-06-01 00:00:00.0",
"tot": "2023-06-01 00:15:00.0",
```

De data mapping hiervan is `Verkeersmeting.fenomeenTijd`. 

```json
"Verkeersmeting.fenomeenTijd": {
        "@type": "time:ProperInterval",
        "time:hasBeginning": {
          "@type": "time:Instant",
          "time:inXSDDateTime": {
            "@type": "xml-schema:dateTime",
            "@value": "20230601T00:00:00.000"
          }
        },
        "time:hasEnd": {
          "@type": "time:Instant",
          "time:inXSDDateTime": {
            "@type": "xml-schema:dateTime",
            "@value": "20230601T00:00:15.000"
          }
        }
      }
```