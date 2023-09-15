---
layout: default
parent: Fietstelpunten
title: OSLO mapping
nav_order: 4
---

# OSLO mapping

Momenteel bevat de context file "https://data.vlaanderen.be/doc/applicatieprofiel/verkeersmetingen/ontwerpstandaard/2023-03-14/context/Verkeersmetingen-ap.jsonld" nog steeds issues (fixme.be e.d.). Dit is doorgegeven aan het OSLO team.

```json
{
  "@context": [
    "https://data.vlaanderen.be/doc/applicatieprofiel/verkeersmetingen/ontwerpstandaard/2023-03-14/context/Verkeersmetingen-ap.jsonld",
    "https://data.vlaanderen.be/doc/applicatieprofiel/sensoren-en-bemonstering/kandidaatstandaard/2022-04-28/context/ap-sensoren-en-bemonstering.jsonld",
    "https://data.vlaanderen.be/doc/applicatieprofiel/observaties-en-metingen/kandidaatstandaard/2022-04-28/context/ap-observaties-en-metingen.jsonld",
    "https://raw.githubusercontent.com/samuvack/context/main/DCAT_context.json",
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

      "cl-vrt": "https://data.vlaanderen.be/doc/conceptscheme/VkmVoertuigTypes/",
      "cl-vkt": "https://data.vlaanderen.be/doc/conceptscheme/VkmVerkeersKenmerkType/",
      "cl-trt": "https://inspire.ec.europa.eu/codelist/LinkDirectionValue/",
      "cl-mit": "https://data.vlaanderen.be/doc/conceptscheme/VkmMeetInstrumentType/",
      "cl-op": "https://data.vlaanderen.be/doc/conceptscheme/VkmObservatieProcedure/",
      "cl-access": "http://publications.europa.eu/resource/authority/access-right/"
    }
  ],
  "@graph": [
    {
      "@id": "_:tellusdata001",
      "@type": "Dataset",
      "Dataset.titel": {
        "@language": "nl",
        "@value": "Fietstellingen - Agentschap Wegen en Verkeer"
      },
      "Dataset.beschrijving": [
        {
          "@language": "nl",
          "@value": "Deze dataset omvat zowel de automatische fietstellingen van AWV, als de locaties waar de tellingen plaatsvinden."
        }
      ],
      "Dataset.toegankelijkheid": "cl-access:PUBLIC",
      "Dataset.trefwoord": [
        {
          "@language": "nl",
          "@value": "fietstellingen"
        }
      ]
    },
    {
      "@id": "_:vrm001",
      "@type": "Verkeersmeting",
      "Observatie.geobserveerdKenmerk": {
        "@type": "Verkeerskenmerk",
        "Verkeerskenmerk.type": "cl-vkt:aantal",
        "Verkeerskenmerk.voertuigType": "cl-vrt:fiets"
      },
      "Telling.resultaat": 60,
      "Observatie.uitgevoerdDoor": "_:mti001",
      "Observatie.geobserveerdObject": {
        "@type": "Verkeersmeetpunt",
        "Observatie.geobserveerdObject": {
          "@type": "Verkeersmeetpunt",
          "Bemonsteringspunt.geometrie": {
            "@type": "Punt",
            "Geometrie.gml": {
              "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/4326\"><gml:coordinates>50.91618331151478,4.456121776137429, offset(m)</gml:coordinates><gml:Point>",
              "@type": "geosparql:gmlLiteral"
            }
          },
          "Bemonsteringsobject.bemonsterdObject": "_:rri001"
        },
        "Observatie.fenomeentijd": {
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
      }
    },
    {
      "@id": "_:rri001",
      "@type": "Rijrichting",
      "Rijrichting.netwerkreferentie": {
        "@type": "LineaireReferentie",
        "Netwerkreferentie.element": "_:wgs001",
        "Linkreferentie.toepassingsRichting": "cl-trt:beide"
      },
      "Rijrichting.rijrichting": "cl-trt:beide"
    },
    {
      "@id": "_:wgs001",
      "@type": "Wegsegment",
      "Wegsegment.beginknoop": "_:wgkn001",
      "Wegsegment.eindknoop": "_:wgkn002",
      "Wegsegment.geometriemiddenlijn":{
        "@type": "LineString",
        "Geometrie.wkt": {
          "@value": "LINESTRING (30 10, 10 30, 40 40)",
          "@type": "geosparql:wktLiteral"
        }
      }
    },
    {
      "@id": "_:wgkn001",
      "@type": "Wegknoop",
      "Wegknoop.geometrie": {
        "@type": "Punt",
        "Geometrie.gml": {
          "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/4326\"><gml:coordinates>14.13421178,46.15023795</gml:coordinates><gml:Point>",
          "@type": "geosparql:gmlLiteral"
        }
      }
    },
    {
      "@id": "_:wgkn002",
      "@type": "Wegknoop",
      "Wegknoop.geometrie": {
        "@type": "Punt",
        "Geometrie.gml": {
          "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/4326\"><gml:coordinates>17.13421178,49.15023795</gml:coordinates><gml:Point>",
          "@type": "geosparql:gmlLiteral"
        }
      }
    },
    {
      "@id": "_:mti001",
      "@type": "Sensor",
      "Systeem.type": "cl-mit:fietstelslang",
      "Sensor.implementeert": {
        "@type": "Observatieproceduretype",
        "Observatieprocedure.type": "cl-op:type"
      }
    }
  ]
}
```
