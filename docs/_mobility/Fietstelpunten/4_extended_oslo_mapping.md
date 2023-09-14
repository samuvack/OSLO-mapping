---
layout: default
parent: Fietstelpunten
title: extended OSLO mapping
nav_order: 5
---

# extended OSLO mapping

```json
[
  {
    "@id": "_:tellusdata001",
    "@type": ["http://www.w3.org/ns/dcat#Dataset"],
    "http://purl.org/dc/terms/description": [
      {
        "@language": "nl",
        "@value": "Deze dataset omvat zowel de automatische fietstellingen van AWV, als de locaties waar de tellingen plaatsvinden."
      }
    ],
    "http://purl.org/dc/terms/title": [
      {
        "@language": "nl",
        "@value": "Fietstellingen - Agentschap Wegen en Verkeer"
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
        "@value": "fietstellingen"
      }
    ]
  },
  {
    "@id": "_:vrm001",
    "@type": ["https://data.vlaanderen.be/ns/verkeersmetingen#Verkeersmeting"],
    "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.observedProperty": [
      {
        "@type": [
          "https://data.vlaanderen.be/ns/verkeersmetingen#Verkeerskenmerk"
        ],
        "https://data.vlaanderen.be/ns/verkeersmetingen#type": [
          {
            "@id": "cl-vkt:aantalvoertuigen"
          }
        ],
        "https://data.vlaanderen.be/ns/verkeersmetingen#voertuigType": [
          {
            "@id": "cl-vrt:fiets"
          }
        ]
      }
    ],
    "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.featureOfInterest": [
      {
        "@type": [
          "https://data.vlaanderen.be/ns/verkeersmetingen#Verkeersmeetpunt"
        ],
        "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.phenomenonTime": [
          {
            "@type": ["http://www.w3.org/2006/time#ProperInterval"],
            "http://www.w3.org/2006/time#hasBeginning": [
              {
                "@type": ["http://www.w3.org/2006/time#Instant"],
                "http://www.w3.org/2006/time#inXSDDateTime": [
                  {
                    "@type": "xml-schema:dateTime",
                    "@value": "20230601T00:00:00.000"
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
                    "@value": "20230601T00:00:15.000"
                  }
                ]
              }
            ]
          }
        ],
        "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.featureOfInterest": [
          {
            "@type": [
              "https://data.vlaanderen.be/ns/verkeersmetingen#Verkeersmeetpunt"
            ],
            "http://def.isotc211.org/iso19156/2011/SamplingFeature#SF_SamplingFeature.sampledFeature": [
              {
                "@id": "_:rri001"
              }
            ],
            "http://def.isotc211.org/iso19156/2011/SamplingPoint#SF_SamplingPoint.shape": [
              {
                "@type": ["http://www.opengis.net/ont/sf#Point"],
                "http://www.opengis.net/ont/geosparql#asGML": [
                  {
                    "@type": "http://www.opengis.net/ont/geosparql#gmlLiteral",
                    "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/4326\"><gml:coordinates>50.91618331151478,4.456121776137429</gml:coordinates><gml:Point>"
                  }
                ]
              }
            ]
          }
        ]
      }
    ],
    "https://data.vlaanderen.be/ns/observaties-en-metingen#Observatie.uitgevoerdDoor": [
      {
        "@id": "_:mti001"
      }
    ],
    "http://def.isotc211.org/iso19156/2011/CountObservation#OM_CountObservation.result": [
      {
        "@type": "http://www.w3.org/2001/XMLSchema#integer",
        "@value": 60
      }
    ]
  },
  {
    "@id": "_:rri001",
    "@type": ["https://data.vlaanderen.be/ns/weg#Rijrichting"],
    "https://data.vlaanderen.be/ns/weg#rijrichting": [
      {
        "@id": "cl-trt:beide"
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
            "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/4326\"><gml:coordinates>14.13421178,46.15023795</gml:coordinates><gml:Point>"
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
            "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/4326\"><gml:coordinates>17.13421178,49.15023795</gml:coordinates><gml:Point>"
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
            "@id": "cl-opt:type"
          }
        ]
      }
    ],
    "http://purl.org/dc/terms/type": [
      {
        "@id": "cl-mit:fietstelslang"
      }
    ]
  }
]
```
