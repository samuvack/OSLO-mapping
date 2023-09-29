---
layout: default
title: Stap voor stap
parent: Brugge
nav_order: 2
---

# Context

De @context sleutel definieert de context waarin de termen in het document worden geïnterpreteerd. Hier worden zowel naar externe contexten (URL's) als codelijsten verwezen.

Externe contexten: De eerste twee URL's verwijzen naar applicatieprofielen die specifieke termen en definities bevatten voor sensoren, bemonstering, observaties en metingen.

```
"https://data.vlaanderen.be/doc/applicatieprofiel/sensoren-en-bemonstering/kandidaatstandaard/2022-04-28/context/ap-sensoren-en-bemonstering.jsonld",
"https://data.vlaanderen.be/doc/applicatieprofiel/observaties-en-metingen/kandidaatstandaard/2022-04-28/context/ap-observaties-en-metingen.jsonld"

```

Codelijsten: Dit is een lijst van prefixen die worden gebruikt om termen in het document korter en leesbaarder te maken. Bijvoorbeeld, time verwijst naar het W3C Time Ontology, en qudt-schema verwijst naar het QUDT schema voor eenheden en dimensies.

```
"time": "http://www.w3.org/2006/time#",
"qudt-schema": "https://qudt.org/schema/qudt/",
"xml-schema": "http://www.w3.org/2001/XMLSchema#",
"geosparql": "http://www.opengis.net/ont/geosparql#",
"cl-bpt": "https://example.com/concept/bemonsteringsproceduretype/",
"cl-bet": "https://example.com/concept/bemonsteraartype/",
"cl-bco": "https://example.com/concept/bemonsteringsconditietype/",
"cl-ovt": "https://example.com/concept/observatieverzamelingtype/",
"cl-obt": "https://example.com/concept/observatietype/",
"cl-wrt": "https://example.com/concept/weertype/",
"cl-idt": "https://example.com/concept/identificatortype/",
"cl-mat": "https://example.com/concept/materiaaltype/",
"cl-mot": "https://example.com/concept/monstertype/",
"cl-fch": "https://data.omgeving.vlaanderen.be/id/concept/fysico-chemisch/",
"qudt-unit": "https://qudt.org/vocab/unit/"
```

# Graph 

De @graph sleutel bevat een lijst van objecten die de daadwerkelijke data van het document vertegenwoordigen. Elk object heeft een @type dat het type van het object aangeeft.

## Tijdstip

Het bemonsteringsgebeurtenis bevat details zoals het tijdstip van bemonstering:
```json
{"datum staalname":"11/01/2021"}
```

Het [Oslo model observaties en metingen](https://data.vlaanderen.be/doc/applicatieprofiel/observaties-en-metingen/kandidaatstandaard/2022-04-28/context/ap-observaties-en-metingen.jsonld) definieert termen zoals Bemonstering, bemonsteringstijdstip, time:Instant en time:inXSDDateTime om de concepten en relaties rond bemonstering uit te drukken. Het "Bemonstering.bemonsteringstijdstip" is hierbij van het type "time:Instant":

```json
"Bemonstering.bemonsteringstijdstip": {
    "@type": "time:Instant",
    "time:inXSDDateTime": {
        "@type": "xml-schema:dateTime",
        "@value": "20210111T12:05:51.000"
}
```

## Meting oppervlakte water

```json
"Waterkwaliteit":
{
    "Temperatuur(water)": 3.6,
}
```

```json
{
    "@id": "_:obs001",
    "@type": "Observatie",
    "Observatie.type": "cl-obt:metingterplaatse",
    "Observatie.kenmerktype": "cl-fch:0030",
    "Observatie.resultaat": {
        "@type": "Maat",
        "Maat.maat": {
            "@type": "KwantitatieveWaarde",
            "KwantitatieveWaarde.waarde": 3.6,
            "KwantitatieveWaarde.standaardEenheid": {
                "@type": "qudt-schema:Unit",
                "@id": "qudt-unit:DEG_C"
            }
        }
    }
}
```
## Weersmeting
```json
        {
            "@id": "_:wra001",
            "@type": "Observatieverzameling",
            "dcterms:type": "cl-ovt:weerrapport",
            "Observatieverzameling.geobserveerdObject": "_:mpt001",
            "Observatieverzameling.heeftLid": [
                "_:wob001",
                ""
            ]
        },
        {
            "@id": "_:wob001",
            "@type": "Observatie",
            "Observatie.type": "cl-obt:weerobservatie",
            "Observatie.kenmerktype": "cl-wrt:zon",
            "Observatie.fenomeentijd": {
                "@type": "time:Instant",
                "time:inXSDDateTime": {
                    "@type": "xml-schema:dateTime",
                    "@value": "20210111T12:05:51.000"
                }
            },
            "Observatie.resultaat": "cl-wrt:zon/bewolkt"
        }
```







Beschrijft een bemonsteringsgebeurtenis. Het bevat details zoals het tijdstip van bemonstering, het object dat is bemonsterd, de organisatie die de bemonstering heeft uitgevoerd, de gebruikte procedure en het resultaat van de bemonstering.

## Monster

Dit object vertegenwoordigt een fysiek monster dat is genomen tijdens de bemonstering. Het bevat details zoals het type materiaal, het tijdstip van bemonstering en een unieke identificator.

## Meetpunt/Bemonsteringspunt

Dit object beschrijft een specifiek punt waar metingen of bemonsteringen worden uitgevoerd. Het bevat een identificator, geometrische gegevens en beschrijvende informatie.

## Observatieverzameling

Dit object groepeert meerdere observaties. Er zijn twee soorten observatieverzamelingen in dit document: één voor metingen ter plaatse en één voor weerobservaties.

## Observatie

Dit object beschrijft een specifieke observatie of meting. Het bevat details zoals het type observatie, het kenmerk dat wordt gemeten, en het resultaat van de observatie.