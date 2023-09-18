---
layout: default
parent: Telraam
title: extended OSLO mapping
nav_order: 5
---

# extended OSLO mapping

```json
[
  {
    "@id": "_:dataset001",
    "@type": ["http://www.w3.org/ns/dcat#Dataset"],
    "http://purl.org/dc/terms/description": [
      {
        "@language": "nl",
        "@value": "Telraam is een oplossing (met burgers) voor het verzamelen van multimodale verkeersgegevens met een speciaal gebouwd, betaalbaar en gebruiksvriendelijk toestel."
      },
      {
        "@language": "en",
        "@value": "Telraam is your citizen-powered solution for collecting multi-modal traffic data with a purpose-built, affordable, and user-friendly device."
      }
    ],
    "http://purl.org/dc/terms/title": [
      {
        "@language": "nl",
        "@value": "Telraam sample 1"
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
        "@value": "multimodale verkeersgegevens"
      }
    ]
  },
  {
    "@id": "_:wgs426009",
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
    ],
    "https://data.vlaanderen.be/ns/weg#middellijnGeometrie": [
      {
        "http://www.opengis.net/ont/geosparql#asGML": [
          {
            "@type": "http://www.opengis.net/ont/geosparql#gmlLiteral",
            "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/4326\"><gml:coordinates>50.9346197016993 4.04451041920408,50.9346499094883 4.04468516398887,50.9346736897766 4.04476128017613, 50.9347048165154 4.04486091154096,50.9347897018035 4.0450104190652,50.9348297017355 4.04508041942127,50.9349798325647 4.04536795581668,50.9350979049717 4.04561050090522, 50.9351073291995 4.04563353497237,50.9351797011571 4.04581042002322</gml:coordinates><gml:Point>"
          }
        ]
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
            "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/4326\"><gml:coordinates>50.9346197016993 4.0445104192040</gml:coordinates><gml:Point>"
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
            "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/4326\"><gml:coordinates>50.9351797011571 4.04581042002322</gml:coordinates><gml:Point>"
          }
        ]
      }
    ]
  },
  {
    "@id": "_:vkmfiets001",
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
            "@id": "https://data.vlaanderen.be/doc/concept/VkmVoertuigType/fiets"
          }
        ]
      }
    ],
    "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.featureOfInterest": [
      {
        "@id": "_:wgs426009"
      }
    ],
    "https://data.vlaanderen.be/ns/observaties-en-metingen#Verkeersmeting.uitgevoerdDoor": [
      {
        "@id": "_:mti001"
      }
    ],
    "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.result": [
      {
        "@type": "http://def.isotc211.org/iso19103/2005/RecordsAndClassMetadata#Any",
        "@value": 33.3209922251018
      }
    ],
    "http://purl.org/dc/terms/memberOf": [
      {
        "@value": "_:dataset001"
      }
    ]
  },
  {
    "@id": "_:vkmvoet001",
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
            "@id": "https://data.vlaanderen.be/doc/concept/VkmVoertuigType/voetganger"
          }
        ]
      }
    ],
    "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.featureOfInterest": [
      {
        "@id": "_:wgs426009"
      }
    ],
    "https://data.vlaanderen.be/ns/observaties-en-metingen#Verkeersmeting.uitgevoerdDoor": [
      {
        "@id": "_:mti001"
      }
    ],
    "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.result": [
      {
        "@type": "http://def.isotc211.org/iso19103/2005/RecordsAndClassMetadata#Any",
        "@value": 33.3209922251018
      }
    ],
    "http://purl.org/dc/terms/memberOf": [
      {
        "@value": "_:dataset001"
      }
    ]
  },
  {
    "@id": "_:vkmzwaar001",
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
            "@id": "https://data.vlaanderen.be/doc/concept/VkmVoertuigType/vrachtwagen"
          }
        ]
      }
    ],
    "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.featureOfInterest": [
      {
        "@id": "_:wgs426009"
      }
    ],
    "https://data.vlaanderen.be/ns/observaties-en-metingen#Verkeersmeting.uitgevoerdDoor": [
      {
        "@id": "_:mti001"
      }
    ],
    "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.result": [
      {
        "@type": "http://def.isotc211.org/iso19103/2005/RecordsAndClassMetadata#Any",
        "@value": 26.6567937800814
      }
    ],
    "http://purl.org/dc/terms/memberOf": [
      {
        "@value": "_:dataset001"
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
        "@id": "_:wgs426009"
      }
    ],
    "https://data.vlaanderen.be/ns/observaties-en-metingen#Verkeersmeting.uitgevoerdDoor": [
      {
        "@id": "_:mti001"
      }
    ],
    "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.result": [
      {
        "@type": "http://def.isotc211.org/iso19103/2005/RecordsAndClassMetadata#Any",
        "@value": 277.230655312846
      }
    ]
  },
  {
    "@id": "_:vmtauto001",
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
        "@id": "_:wgs426009"
      }
    ],
    "https://data.vlaanderen.be/ns/observaties-en-metingen#Verkeersmeting.uitgevoerdDoor": [
      {
        "@id": "_:mti001"
      }
    ],
    "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.result": [
      {
        "@type": "http://def.isotc211.org/iso19103/2005/RecordsAndClassMetadata#Any",
        "@value": 277.230655312846
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
            "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/4326\"><gml:coordinates>virtual_x,virtual_y, offset(m)</gml:coordinates><gml:Point>"
          }
        ]
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
                "@value": "20210930T06:00:00.000"
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
                "@value": "20210930T07:00:00.000"
              }
            ]
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
        "@id": "https://data.vlaanderen.be/doc/concept/VkmMeetInstrumentType/telraam"
      }
    ]
  }
]
```
