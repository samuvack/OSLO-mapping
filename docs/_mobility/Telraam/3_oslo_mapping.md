---
layout: default
parent: Telraam
title: OSLO mapping
nav_order: 4
---

# OSLO mapping

```json
{
  "@context": [
    "https://data.vlaanderen.be/doc/applicatieprofiel/verkeersmetingen/ontwerpstandaard/2023-03-14/context/Verkeersmetingen-ap.jsonld",
    "https://data.vlaanderen.be/doc/applicatieprofiel/sensoren-en-bemonstering/kandidaatstandaard/2022-04-28/context/ap-sensoren-en-bemonstering.jsonld",
    "https://data.vlaanderen.be/doc/applicatieprofiel/observaties-en-metingen/kandidaatstandaard/2022-04-28/context/ap-observaties-en-metingen.jsonld",
    "https://data.vlaanderen.be/doc/applicatieprofiel/GEODCAT-AP-VL/erkendestandaard/2022-04-21/context/geodcatap-vlaanderen.jsonld",
    "https://data.vlaanderen.be/doc/applicatieprofiel/generiek-basis/zonderstatus/2019-07-01/context/generiek-basis.jsonld",
    {
      "schema": "http://schema.org/",
      "dct": "http://purl.org/dc/terms/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "geosparql": "http://www.opengis.net/ont/geosparql#",
      "qudt-unit": "http://qudt.org/vocab/unit/",
      "qudt-schema": "https://qudt.org/schema/qudt/",
      "dcterms": "http://purl.org/dc/terms/",
      "time": "http://www.w3.org/2006/time#",
      "Verkeersmeting.resultaat": {
        "@type": "http://def.isotc211.org/iso19103/2005/RecordsAndClassMetadata#Any",
        "@id": "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.result"
      },

      "cl-vrt": "https://data.vlaanderen.be/doc/conceptscheme/VkmVoertuigType/",
      "cl-vkt": "https://data.vlaanderen.be/doc/conceptscheme/VkmVerkeersKenmerkType/",
      "cl-mit": "https://data.vlaanderen.be/doc/conceptscheme/VkmMeetInstrumentType/",
      "cl-op": "https://data.vlaanderen.be/doc/conceptscheme/VkmObservatieProcedure/",
      "cl-access": "http://publications.europa.eu/resource/authority/access-right/"
    }
  ],
  "@graph": [
    {
      "@id": "_:dataset001",
      "@type": "Dataset",
      "Dataset.titel": {
        "@language": "nl",
        "@value": "Telraam sample 1"
      },
      "Dataset.beschrijving": [
        {
          "@language": "nl",
          "@value": "Telraam is een oplossing (met burgers) voor het verzamelen van multimodale verkeersgegevens met een speciaal gebouwd, betaalbaar en gebruiksvriendelijk toestel."
        },
        {
          "@language": "en",
          "@value": "Telraam is your citizen-powered solution for collecting multi-modal traffic data with a purpose-built, affordable, and user-friendly device."
        }
      ],
      "Dataset.toegankelijkheid": "cl-access:PUBLIC",
      "Dataset.trefwoord": [
        {
          "@language": "nl",
          "@value": "multimodale verkeersgegevens"
        }
      ]
    },

    {
      "@id": "_:wgs426009",
      "@type": "Wegsegment",
      "Wegsegment.geometriemiddenlijn": {
        "Geometrie.gml": {
          "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/4326\">50.9346197016993 4.04451041920408,50.9346499094883 4.04468516398887,50.9346736897766 4.04476128017613, 50.9347048165154 4.04486091154096,50.9347897018035 4.0450104190652,50.9348297017355 4.04508041942127,50.9349798325647 4.04536795581668,50.9350979049717 4.04561050090522, 50.9351073291995 4.04563353497237,50.9351797011571 4.04581042002322<gml:coordinates></gml:coordinates><gml:Point>",
          "@type": "geosparql:gmlliteral"
        }
      }
    },
    {
      "@id": "_:vkmfiets001",
      "@type": "Verkeersmeting",
      "Observatie.geobserveerdKenmerk": {
        "@type": "Verkeerskenmerk",
        "Verkeerskenmerk.type": "cl-vkt:aantal",
        "Verkeerskenmerk.voertuigType": "cl-vrt:fiets"
      },
      "Observatie.geobserveerdObject": "_:wgs426009",
      "Observatie.fenomeentijd": ":_fenomtime001",
      "Verkeersmeting.resultaat": 33.3209922251018,
      "Observatie.uitgevoerdDoor": "_:mti001",
      "dct:memberOf": "_:dataset001"
    },
    {
      "@id": "_:vkmvoet001",
      "@type": "Verkeersmeting",
      "Observatie.geobserveerdKenmerk": {
        "@type": "Verkeerskenmerk",
        "Verkeerskenmerk.type": "cl-vkt:aantal",
        "Verkeerskenmerk.voertuigType": "cl-vrt:voetganger"
      },
      "Observatie.geobserveerdObject": "_:wgs426009",
      "Observatie.fenomeentijd": ":_fenomtime001",
      "Verkeersmeting.resultaat": 33.3209922251018,
      "Observatie.uitgevoerdDoor": "_:mti001",
      "dct:memberOf": "_:dataset001"
    },
    {
      "@id": "_:vkmzwaar001",
      "@type": "Verkeersmeting",
      "Observatie.geobserveerdKenmerk": {
        "@type": "Verkeerskenmerk",
        "Verkeerskenmerk.type": "cl-vkt:aantal",
        "Verkeerskenmerk.voertuigType": "cl-vrt:zwaarverkeer"
      },
      "Observatie.geobserveerdObject": "_:wgs426009",
      "Observatie.fenomeentijd": ":_fenomtime001",
      "Verkeersmeting.resultaat": 26.6567937800814,
      "Observatie.uitgevoerdDoor": "_:mti001",
      "dct:memberOf": "_:dataset001"
    },
    {
      "@id": "_:vkmauto001",
      "@type": "Verkeersmeting",
      "Observatie.geobserveerdKenmerk": {
        "@type": "Verkeerskenmerk",
        "Verkeerskenmerk.type": "cl-vkt:aantal",
        "Verkeerskenmerk.voertuigType": "cl-vrt:auto"
      },
      "Observatie.geobserveerdObject": "_:wgs426009",
      "Observatie.fenomeentijd": ":_fenomtime001",
      "Verkeersmeting.resultaat": 277.230655312846,
      "Observatie.uitgevoerdDoor": "_:mti001"
    },
    {
      "@id": "_:vmtauto001",
      "@type": "Verkeersmeting",
      "Observatie.geobserveerdKenmerk": {
        "@type": "Verkeerskenmerk",
        "Verkeerskenmerk.type": "cl-vkt:aantal",
        "Verkeerskenmerk.voertuigType": "cl-vrt:auto"
      },
      "Observatie.geobserveerdObject": "_:wgs426009",
      "Observatie.fenomeentijd": ":_fenomtime001",
      "Verkeersmeting.resultaat": 277.230655312846,
      "Observatie.uitgevoerdDoor": "_:mti001"
    },
    {
      "@id": "_:fenomtime001",
      "Observatie.fenomeentijd": {
        "@type": "time:ProperInterval",
        "time:hasBeginning": {
          "@type": "time:Instant",
          "time:inXSDDateTime": {
            "@type": "xml-schema:dateTime",
            "@value": "20210930T06:00:00.000"
          }
        },
        "time:hasEnd": {
          "@type": "time:Instant",
          "time:inXSDDateTime": {
            "@type": "xml-schema:dateTime",
            "@value": "20210930T07:00:00.000"
          }
        }
      }
    },
    {
      "@id": "_:mti001",
      "@type": "Sensor",
      "Systeem.type": "cl-mit:telraam",
      "Sensor.implementeert": {
        "@type": "Observatieproceduretype",
        "Observatieprocedure.type": "cl-op:type"
      }
    }
  ]
}
```

```note
Hierbij wordt gekozen om de rijrichting niet te omschrijven, net zoals dit niet gedaan wordt in de brondataset

```

Dit zou eventueel wel kunnen, door dit element toe te voegen:

```json
{
  "@id": "_:rri001",
  "@type": "Rijrichting",
  "Rijrichting.netwerkreferentie": {
    "@type": "LineaireReferentie",
    "LineaireReferentie.vanPositie": {
      "@type": "Lengte",
      "KwantitatieveWaarde.waarde": "0",
      "KwantitatieveWaarde.standaardEenheid": {
        "@value": "m",
        "@type": "ucum:ucumunit"
      }
    },
    "LineaireReferentie.totPositie": {
      "@type": "Lengte",
      "KwantitatieveWaarde.waarde": "600",
      "KwantitatieveWaarde.standaardEenheid": {
        "@value": "m",
        "@type": "ucum:ucumunit"
      }
    },
    "Netwerkreferentie.element": "_:wgs426009",
    "Linkreferentie.toepassingsRichting": "cl-trt:inDirection"
  },
  "Rijrichting.rijrichting": "cl-trt:inDirection"
}
```
