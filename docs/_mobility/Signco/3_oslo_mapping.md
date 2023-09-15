---
layout: default
parent: Signco
title: OSLO mapping
nav_order: 4
---

# OSLO mapping

```json
{
  "@context": [
    "https://raw.githubusercontent.com/samuvack/context/main/Verkeersmetingen-ap.jsonld",
    "https://data.vlaanderen.be/doc/applicatieprofiel/sensoren-en-bemonstering/kandidaatstandaard/2022-04-28/context/ap-sensoren-en-bemonstering.jsonld",
    "https://data.vlaanderen.be/doc/applicatieprofiel/observaties-en-metingen/kandidaatstandaard/2022-04-28/context/ap-observaties-en-metingen.jsonld",
    "https://raw.githubusercontent.com/samuvack/context/main/wegenregister.jsonld",
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
      "adms": "http://www.w3.org/ns/adms#",
      "Verkeersmeting.resultaat": {
        "@type": "http://def.isotc211.org/iso19103/2005/RecordsAndClassMetadata#Any",
        "@id": "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.result"
      },

      "cl-vrt": "https://data.vlaanderen.be/doc/concept/VkmVoertuigType/",
      "cl-vkt": "https://data.vlaanderen.be/doc/concept/VkmVerkeersKenmerkType/",
      "cl-trt": "https://inspire.ec.europa.eu/codelist/LinkDirectionValue/",
      "cl-mit": "https://data.vlaanderen.be/doc/concept/VkmMeetInstrumentType/",
      "cl-op": "https://data.vlaanderen.be/doc/concept/VkmObservatieProcedure/",
      "cl-access": "http://publications.europa.eu/resource/authority/access-right/"
    }
  ],
  "@graph": [
    {
      "@id": "_:Signco001",
      "@type": "Dataset",
      "Dataset.titel": {
        "@language": "nl",
        "@value": "Signco."
      },
      "Dataset.beschrijving": [
        {
          "@language": "nl",
          "@value": ""
        }
      ],
      "Dataset.toegankelijkheid": "cl-access:PUBLIC",
      "Dataset.trefwoord": [
        {
          "@language": "nl",
          "@value": "Signco"
        }
      ]
    },
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
        "Netwerkreferentie.element": "_:wgs001",
        "Linkreferentie.toepassingsRichting": "cl-trt:inDirection"
      },
      "Rijrichting.rijrichting": "cl-trt:inDirection"
    },
    {
      "@id": "_:rri002",
      "@type": "Rijrichting",
      "Rijrichting.netwerkreferentie": {
        "@type": "LineaireReferentie",
        "Netwerkreferentie.element": "_:wgs001",
        "Linkreferentie.toepassingsRichting": "cl-trt:tegengesteld"
      },
      "Rijrichting.rijrichting": "cl-trt:tegengesteld"
    },

    {
      "@id": "_:wgs001",
      "@type": "Wegsegment",
      "Wegsegment.beginknoop": "_:wgkn001",
      "Wegsegment.eindknoop": "_:wgkn002",
      "Wegsegment.geometriemiddenlijn": {
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
          "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/4326\"><gml:coordinates></gml:coordinates><gml:Point>",
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
          "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/4326\"><gml:coordinates></gml:coordinates><gml:Point>",
          "@type": "geosparql:gmlLiteral"
        }
      }
    },
    {
      "@id": "_:vkmauto001",
      "@type": "Verkeersmeting",
      "Observatie.geobserveerdKenmerk": {
        "@type": "Verkeerskenmerk",
        "Verkeerskenmerk.type": "cl-vkt:aantal",
        "Verkeerskenmerk.voertuigType": "cl-vrt:auto"
      },
      "Observatie.geobserveerdObject": "_:rri001",
      "Observatie.fenomeentijd": ":_fenomtime001",
      "Verkeersmeting.resultaat": 30,
      "Observatie.uitgevoerdDoor": "_:mti001",
      "Verkeersmeetpunt": "_:mpt001",
      "dct:memberOf": "_:Signco001"
    },
    {
      "@id": "_:vkmauto001",
      "@type": "Verkeersmeting",
      "Observatie.geobserveerdKenmerk": {
        "@type": "Verkeerskenmerk",
        "Verkeerskenmerk.type": "cl-vkt:aantal",
        "Verkeerskenmerk.voertuigType": "cl-vrt:auto"
      },
      "Observatie.geobserveerdObject": "_:rri002",
      "Observatie.fenomeentijd": ":_fenomtime001",
      "Verkeersmeting.resultaat": 210,
      "Observatie.uitgevoerdDoor": "_:mti001",
      "Verkeersmeetpunt": "_:mpt001",
      "dct:memberOf": "_:Signco001"
    },
    {
      "@id": "_:fenomtime001",
      "Observatie.fenomeentijd": {
        "@type": "time:ProperInterval",
        "time:hasBeginning": {
          "@type": "time:Instant",
          "time:inXSDDateTime": {
            "@type": "xml-schema:dateTime",
            "@value": "20161122T09:00:00.000Z"
          }
        },
        "time:hasEnd": {
          "@type": "time:Instant",
          "time:inXSDDateTime": {
            "@type": "xml-schema:dateTime",
            "@value": "20161122T10:00:00.000Z"
          }
        }
      }
    },
    {
      "@id": "_:mpt001",
      "@type": "Verkeersmeetpunt",
      "Bemonsteringspunt.geometrie": {
        "@type": "Punt",
        "Geometrie.gml": {
          "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/4326\"><gml:coordinates>51.041935,4.35714, offset(m)</gml:coordinates><gml:Point>",
          "@type": "geosparql:gmlLiteral"
        }
      }
    },

    {
      "@id": "_:mti001",
      "@type": "Sensor",
      "Systeem.type": "cl-mit:atc",
      "Sensor.implementeert": {
        "@type": "Observatieproceduretype",
        "Observatieprocedure.type": "cl-op:type"
      }
    }
  ]
}
```
