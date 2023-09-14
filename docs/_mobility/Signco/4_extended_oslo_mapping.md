---
layout: default
parent: Signco
title: extended OSLO mapping
nav_order: 5
---

# extended OSLO mapping

```json
[
  {
    "@id": "_:Signco001",
    "@type": ["http://www.w3.org/ns/dcat#Dataset"],
    "http://purl.org/dc/terms/description": [
      {
        "@language": "nl",
        "@value": ""
      }
    ],
    "http://purl.org/dc/terms/title": [
      {
        "@language": "nl",
        "@value": "Signco."
      }
    ],
    "http://purl.org/dc/terms/accessRights": [
      {
        "@id": "http://publications.europa.eu/resource/authority/access-right/PUBLIC"
      }
    ],
    "http://www.w3.org/ns/dcat#keyword": [
      {
        "@language": "nl",
        "@value": "Signco"
      }
    ]
  },
  {
    "@id": "_:rri001",
    "@type": ["https://data.vlaanderen.be/ns/weg#Rijrichting"],
    "https://data.vlaanderen.be/ns/weg#rijrichting": [
      {
        "@id": "https://inspire.ec.europa.eu/codelist/LinkDirectionValue/inDirection"
      }
    ]
  },
  {
    "@id": "_:rri002",
    "@type": ["https://data.vlaanderen.be/ns/weg#Rijrichting"],
    "https://data.vlaanderen.be/ns/weg#rijrichting": [
      {
        "@id": "https://inspire.ec.europa.eu/codelist/LinkDirectionValue/tegengesteld"
      }
    ]
  },
  {
    "@id": "_:wgs001",
    "@type": ["https://data.vlaanderen.be/ns/weg#Wegsegment"],
    "https://data.vlaanderen.be/ns/netwerk/#beginknoop": [
      {
        "@id": "_:wgkn001"
      }
    ],
    "https://data.vlaanderen.be/ns/netwerk#eindknoop": [
      {
        "@id": "_:wgkn002"
      }
    ]
  },
  {
    "@id": "_:wgkn001",
    "@type": ["https://data.vlaanderen.be/ns/weg#Wegknoop"],
    "https://data.vlaanderen.be/ns/weg#geometrie": [
      {
        "@type": ["http://www.opengis.net/ont/sf#Point"],
        "http://www.opengis.net/ont/geosparql#asGML": [
          {
            "@type": "http://www.opengis.net/ont/geosparql#gmlLiteral",
            "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/4326\"><gml:coordinates></gml:coordinates><gml:Point>"
          }
        ]
      }
    ]
  },
  {
    "@id": "_:wgkn002",
    "@type": ["https://data.vlaanderen.be/ns/weg#Wegknoop"],
    "https://data.vlaanderen.be/ns/weg#geometrie": [
      {
        "@type": ["http://www.opengis.net/ont/sf#Point"],
        "http://www.opengis.net/ont/geosparql#asGML": [
          {
            "@type": "http://www.opengis.net/ont/geosparql#gmlLiteral",
            "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/4326\"><gml:coordinates></gml:coordinates><gml:Point>"
          }
        ]
      }
    ]
  },
  {
    "@id": "_:vkmauto001",
    "@type": ["https://data.vlaanderen.be/ns/verkeersmetingen#Verkeersmeting"],
    "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.phenomenonTime": [
      {
        "@id": ":_fenomtime001"
      }
    ],
    "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.observedProperty": [
      {
        "@type": [
          "https://data.vlaanderen.be/ns/verkeersmetingen#Verkeerskenmerk"
        ],
        "https://data.vlaanderen.be/ns/verkeersmetingen#type": [
          {
            "@id": "https://data.vlaanderen.be/doc/concept/VkmVerkeersKenmerkType/aantal"
          }
        ],
        "https://data.vlaanderen.be/ns/verkeersmetingen#voertuigType": [
          {
            "@id": "https://data.vlaanderen.be/doc/concept/VkmVoertuigType/auto"
          }
        ]
      }
    ],
    "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.featureOfInterest": [
      {
        "@id": "_:rri001"
      }
    ],
    "https://data.vlaanderen.be/ns/observaties-en-metingen#Observatie.uitgevoerdDoor": [
      {
        "@id": "_:mti001"
      }
    ],
    "https://data.vlaanderen.be/ns/verkeersmetingen#Verkeersmeetpunt": [
      {
        "@value": "_:mpt001"
      }
    ],
    "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.result": [
      {
        "@type": "http://def.isotc211.org/iso19103/2005/RecordsAndClassMetadata#Any",
        "@value": 30
      }
    ],
    "http://purl.org/dc/terms/memberOf": [
      {
        "@value": "_:Signco001"
      }
    ]
  },
  {
    "@id": "_:vkmauto001",
    "@type": ["https://data.vlaanderen.be/ns/verkeersmetingen#Verkeersmeting"],
    "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.phenomenonTime": [
      {
        "@id": ":_fenomtime001"
      }
    ],
    "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.observedProperty": [
      {
        "@type": [
          "https://data.vlaanderen.be/ns/verkeersmetingen#Verkeerskenmerk"
        ],
        "https://data.vlaanderen.be/ns/verkeersmetingen#type": [
          {
            "@id": "https://data.vlaanderen.be/doc/concept/VkmVerkeersKenmerkType/aantal"
          }
        ],
        "https://data.vlaanderen.be/ns/verkeersmetingen#voertuigType": [
          {
            "@id": "https://data.vlaanderen.be/doc/concept/VkmVoertuigType/auto"
          }
        ]
      }
    ],
    "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.featureOfInterest": [
      {
        "@id": "_:rri002"
      }
    ],
    "https://data.vlaanderen.be/ns/observaties-en-metingen#Observatie.uitgevoerdDoor": [
      {
        "@id": "_:mti001"
      }
    ],
    "https://data.vlaanderen.be/ns/verkeersmetingen#Verkeersmeetpunt": [
      {
        "@value": "_:mpt001"
      }
    ],
    "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.result": [
      {
        "@type": "http://def.isotc211.org/iso19103/2005/RecordsAndClassMetadata#Any",
        "@value": 210
      }
    ],
    "http://purl.org/dc/terms/memberOf": [
      {
        "@value": "_:Signco001"
      }
    ]
  },
  {
    "@id": "_:fenomtime001",
    "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.phenomenonTime": [
      {
        "@type": ["http://www.w3.org/2006/time#ProperInterval"],
        "http://www.w3.org/2006/time#hasBeginning": [
          {
            "@type": ["http://www.w3.org/2006/time#Instant"],
            "http://www.w3.org/2006/time#inXSDDateTime": [
              {
                "@type": "xml-schema:dateTime",
                "@value": "20161122T09:00:00.000Z"
              }
            ]
          }
        ],
        "http://www.w3.org/2006/time#hasEnd": [
          {
            "@type": ["http://www.w3.org/2006/time#Instant"],
            "http://www.w3.org/2006/time#inXSDDateTime": [
              {
                "@type": "xml-schema:dateTime",
                "@value": "20161122T10:00:00.000Z"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "@id": "_:mpt001",
    "@type": [
      "https://data.vlaanderen.be/ns/verkeersmetingen#Verkeersmeetpunt"
    ],
    "http://def.isotc211.org/iso19156/2011/SamplingPoint#SF_SamplingPoint.shape": [
      {
        "@type": ["http://www.opengis.net/ont/sf#Point"],
        "http://www.opengis.net/ont/geosparql#asGML": [
          {
            "@type": "http://www.opengis.net/ont/geosparql#gmlLiteral",
            "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/4326\"><gml:coordinates>51.041935,4.35714</gml:coordinates><gml:Point>"
          }
        ]
      }
    ]
  },
  {
    "@id": "_:mti001",
    "@type": ["https://www.w3.org/ns/sosa/Sensor"],
    "http://www.w3.org/ns/ssn/implements": [
      {
        "@type": ["http://www.w3.org/2004/02/skos/core#Concept"],
        "http://purl.org/dc/terms/type": [
          {
            "@id": "https://data.vlaanderen.be/doc/concept/VkmObservatieProcedure/type"
          }
        ]
      }
    ],
    "http://purl.org/dc/terms/type": [
      {
        "@id": "https://data.vlaanderen.be/doc/concept/VkmMeetInstrumentType/atc"
      }
    ]
  }
]
```
