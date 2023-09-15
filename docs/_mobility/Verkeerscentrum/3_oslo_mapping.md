---
layout: default
parent: Verkeerscentrum
title: OSLO mapping
nav_order: 4
---

# OSLO mapping

Momenteel bevat de context file "https://raw.githubusercontent.com/samuvack/context/main/Verkeersmetingen-ap.jsonld" nog steeds issues (fixme.be e.d.). Dit is doorgegeven aan het OSLO team.

```json
{
  "@context": [
    "https://raw.githubusercontent.com/samuvack/context/main/Verkeersmetingen-ap.jsonld",
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
      "adms": "http://www.w3.org/ns/adms#",
      "Verkeersmeting.resultaat": {
        "@type": "http://def.isotc211.org/iso19103/2005/RecordsAndClassMetadata#Any",
        "@id": "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.result"
      },

      "cl-rst": "https://data.vlaanderen.be/doc/conceptscheme/VkmRijstrookType/",
      "cl-vrt": "https://data.vlaanderen.be/doc/conceptscheme/VkmVoertuigType/",
      "cl-vkt": "https://data.vlaanderen.be/doc/conceptscheme/VkmVerkeersKenmerkType/",
      "cl-trt": "https://inspire.ec.europa.eu/codelist/LinkDirectionValue/",
      "cl-mit": "https://data.vlaanderen.be/doc/conceptscheme/VkmMeetInstrumentType/",
      "cl-op": "https://data.vlaanderen.be/doc/conceptscheme/VkmObservatieProcedure/",
      "cl-access": "http://publications.europa.eu/resource/authority/access-right/"
    }
  ],
  "@graph": [
    {
      "@id": "_:MIV001",
      "@type": "Dataset",
      "Dataset.titel": {
        "@language": "nl",
        "@value": "MIV - Meten-in-Vlaanderen (MIV) minuutwaarden verkeersmetingen."
      },
      "Dataset.beschrijving": [
        {
          "@language": "nl",
          "@value": "Deze gegevens zijn afkomstig van dubbele meetlussen, hoofdzakelijk op snelwegen in het Vlaams gewest."
        }
      ],
      "Dataset.toegankelijkheid": "cl-access:PUBLIC",
      "Dataset.trefwoord": [
        {
          "@language": "nl",
          "@value": "verkeersmetingen"
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
      "@id": "_:rst001",
      "@type": "Rijstrook",
      "adms:identifier": {
        "@type": "adms:Identifier",
        "skos:notation": {
          "@type": "cl-rst:rechter_rijstrook",
          "@value": "R10"
        }
      },
      "Rijstrook.netwerkreferentie": {
        "@type": "LineaireReferentie",
        "Netwerkreferentie.element": "_:wgs001",
        "Linkreferentie.toepassingsRichting": "cl-trt:inDirection",
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
        }
      },
      "Rijstrook.rijstrook": "R10"
    },
    {
      "@id": "_:wgs001",
      "@type": "Wegsegment",
      "Wegsegment.beginknoop": "_:wgkn001",
      "Wegsegment.eindknoop": "_:wgkn002"
    },
    {
      "@id": "_:wgkn001",
      "@type": "Wegknoop",
      "Wegknoop.geometrie": {
        "@type": "Punt",
        "Geometrie.gml": {
          "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/31370\"><gml:coordinates></gml:coordinates><gml:Point>",
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
          "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/31370\"><gml:coordinates></gml:coordinates><gml:Point>",
          "@type": "geosparql:gmlLiteral"
        }
      }
    },
    {
      "@id": "_:vkmzwaar001",
      "@type": "Verkeersmeting",
      "Observatie.geobserveerdKenmerk": {
        "@type": "Verkeerskenmerk",
        "Verkeerskenmerk.type": "cl-vkt:aantal",
        "Verkeerskenmerk.voertuigType": "cl-vrt:vrachtwagen"
      },
      "Observatie.geobserveerdObject": "_:rst001",
      "Observatie.fenomeentijd": ":_fenomtime001",
      "Verkeersmeting.resultaat": 0,
      "Observatie.uitgevoerdDoor": "_:mti001",
      "Verkeersmeetpunt": "_:mpt001",
      "dct:memberOf": "_:MIV001"
    },
    {
      "@id": "_:vkmzwaar001",
      "@type": "Verkeersmeting",
      "Observatie.geobserveerdKenmerk": {
        "@type": "Verkeerskenmerk",
        "Verkeerskenmerk.type": "cl-vkt:snelheid",
        "Verkeerskenmerk.voertuigType": "cl-vrt:vrachtwagen"
      },
      "Observatie.geobserveerdObject": "_:rst001",
      "Observatie.fenomeentijd": ":_fenomtime001",
      "Verkeersmeting.resultaat": 0,
      "Observatie.uitgevoerdDoor": "_:mti001",
      "Verkeersmeetpunt": "_:mpt001",
      "dct:memberOf": "_:MIV001"
    },
    {
      "@id": "_:vkmauto001",
      "@type": "Verkeersmeting",
      "Observatie.geobserveerdKenmerk": {
        "@type": "Verkeerskenmerk",
        "Verkeerskenmerk.type": "cl-vkt:aantal",
        "Verkeerskenmerk.voertuigType": "cl-vrt:auto"
      },
      "Observatie.geobserveerdObject": "_:rst001",
      "Observatie.fenomeentijd": ":_fenomtime001",
      "Verkeersmeting.resultaat": 0,
      "Observatie.uitgevoerdDoor": "_:mti001",
      "Verkeersmeetpunt": "_:mpt001",
      "dct:memberOf": "_:MIV001"
    },
    {
      "@id": "_:vkmauto001",
      "@type": "Verkeersmeting",
      "Observatie.geobserveerdKenmerk": {
        "@type": "Verkeerskenmerk",
        "Verkeerskenmerk.type": "cl-vkt:snelheid",
        "Verkeerskenmerk.voertuigType": "cl-vrt:auto"
      },
      "Observatie.geobserveerdObject": "_:rst001",
      "Observatie.fenomeentijd": ":_fenomtime001",
      "Verkeersmeting.resultaat": 0,
      "Observatie.uitgevoerdDoor": "_:mti001",
      "Verkeersmeetpunt": "_:mpt001",
      "dct:memberOf": "_:MIV001"
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
      "Verkeersmeting.resultaat": 0,
      "Observatie.uitgevoerdDoor": "_:mti001",
      "Verkeersmeetpunt": "_:mpt001",
      "dct:memberOf": "_:MIV001"
    },
    {
      "@id": "_:fenomtime001",
      "Observatie.fenomeentijd": {
        "@type": "time:ProperInterval",
        "time:hasBeginning": {
          "@type": "time:Instant",
          "time:inXSDDateTime": {
            "@type": "xml-schema:dateTime",
            "@value": "20230801T10:10:00+01:00"
          }
        },
        "time:hasEnd": {
          "@type": "time:Instant",
          "time:inXSDDateTime": {
            "@type": "xml-schema:dateTime",
            "@value": "20230801T11:11:12+02:00"
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
          "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/31370\"><gml:coordinates>144474.5297,208293.5324, offset(m)</gml:coordinates><gml:Point>",
          "@type": "geosparql:gmlLiteral"
        },
        "Geometrie.wkt": {
          "@value": "Point(144474.5297,208293.5324, offset(m))",
          "@type": "geosparql:wktLiteral"
        }
      },

      "Verkeersmeetpunt.rijstrook": "_rst001"
    },

    {
      "@id": "_:mti001",
      "@type": "Sensor",
      "Systeem.type": "cl-mit:verkeersmeting",
      "Sensor.implementeert": {
        "@type": "Observatieproceduretype",
        "Observatieprocedure.type": "cl-op:type"
      }
    }
  ]
}
```
