---
layout: default
parent: Verkeerscentrum
title: extended OSLO mapping
nav_order: 5
---


# extended OSLO mapping




´´´json

[
  {
    "@id": "_:MIV001",
    "@type": [
      "http://www.w3.org/ns/dcat#Dataset"
    ],
    "http://purl.org/dc/terms/description": [
      {
        "@language": "nl",
        "@value": "Deze gegevens zijn afkomstig van dubbele meetlussen, hoofdzakelijk op snelwegen in het Vlaams gewest."
      }
    ],
    "http://purl.org/dc/terms/title": [
      {
        "@language": "nl",
        "@value": "MIV - Meten-in-Vlaanderen (MIV) minuutwaarden verkeersmetingen."
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
        "@value": "verkeersmetingen"
      }
    ]
  },
  {
    "@id": "_:rri001",
    "@type": [
      "https://data.vlaanderen.be/ns/weg#Rijrichting"
    ],
    "https://data.vlaanderen.be/ns/weg#rijrichting": [
      {
        "@id": "https://inspire.ec.europa.eu/codelist/LinkDirectionValue/inDirection"
      }
    ]
  },
  {
    "@id": "_:rst001",
    "@type": [
      "https://data.vlaanderen.be/ns/verkeersmetingen#Rijstrook"
    ],
    "https://data.vlaanderen.be/ns/verkeersmetingen#rijstrook": [
      {
        "@id": "R10"
      }
    ],
    "http://www.w3.org/ns/adms#identifier": [
      {
        "@type": [
          "http://www.w3.org/ns/adms#Identifier"
        ],
        "skos:notation": [
          {
            "@type": "https://data.vlaanderen.be/doc/conceptscheme/VkmRijstrookType/rechter_rijstrook",
            "@value": "R10"
          }
        ]
      }
    ]
  },
  {
    "@id": "_:wgs001",
    "@type": [
      "https://data.vlaanderen.be/ns/weg#Wegsegment"
    ],
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
    "@type": [
      "https://data.vlaanderen.be/ns/weg#Wegknoop"
    ],
    "https://data.vlaanderen.be/ns/weg#geometrie": [
      {
        "@type": [
          "http://www.opengis.net/ont/sf#Point"
        ],
        "http://www.opengis.net/ont/geosparql#asGML": [
          {
            "@type": "http://www.opengis.net/ont/geosparql#gmlliteral",
            "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/31370\"><gml:coordinates></gml:coordinates><gml:Point>"
          }
        ]
      }
    ]
  },
  {
    "@id": "_:wgkn002",
    "@type": [
      "https://data.vlaanderen.be/ns/weg#Wegknoop"
    ],
    "https://data.vlaanderen.be/ns/weg#geometrie": [
      {
        "@type": [
          "http://www.opengis.net/ont/sf#Point"
        ],
        "http://www.opengis.net/ont/geosparql#asGML": [
          {
            "@type": "http://www.opengis.net/ont/geosparql#gmlliteral",
            "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/31370\"><gml:coordinates></gml:coordinates><gml:Point>"
          }
        ]
      }
    ]
  },
  {
    "@id": "_:vkmzwaar001",
    "@type": [
      "https://data.vlaanderen.be/ns/verkeersmetingen#Verkeersmeting"
    ],
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
            "@id": "https://data.vlaanderen.be/doc/conceptscheme/Vkmverkeerskenmerktype/aantal"
          }
        ],
        "https://data.vlaanderen.be/ns/verkeersmetingen#voertuigType": [
          {
            "@id": "https://data.vlaanderen.be/doc/conceptscheme/VkmVoertuigType/zwaarverkeer"
          }
        ]
      }
    ],
    "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.featureOfInterest": [
      {
        "@id": "_:rst001"
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
        "@value": 0
      }
    ],
    "http://purl.org/dc/terms/memberOf": [
      {
        "@value": "_:MIV001"
      }
    ]
  },
  {
    "@id": "_:vkmzwaar001",
    "@type": [
      "https://data.vlaanderen.be/ns/verkeersmetingen#Verkeersmeting"
    ],
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
            "@id": "https://data.vlaanderen.be/doc/conceptscheme/Vkmverkeerskenmerktype/snelheid"
          }
        ],
        "https://data.vlaanderen.be/ns/verkeersmetingen#voertuigType": [
          {
            "@id": "https://data.vlaanderen.be/doc/conceptscheme/VkmVoertuigType/zwaarverkeer"
          }
        ]
      }
    ],
    "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.featureOfInterest": [
      {
        "@id": "_:rst001"
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
        "@value": 0
      }
    ],
    "http://purl.org/dc/terms/memberOf": [
      {
        "@value": "_:MIV001"
      }
    ]
  },
  {
    "@id": "_:vkmauto001",
    "@type": [
      "https://data.vlaanderen.be/ns/verkeersmetingen#Verkeersmeting"
    ],
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
            "@id": "https://data.vlaanderen.be/doc/conceptscheme/Vkmverkeerskenmerktype/aantal"
          }
        ],
        "https://data.vlaanderen.be/ns/verkeersmetingen#voertuigType": [
          {
            "@id": "https://data.vlaanderen.be/doc/conceptscheme/VkmVoertuigType/auto"
          }
        ]
      }
    ],
    "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.featureOfInterest": [
      {
        "@id": "_:rst001"
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
        "@value": 0
      }
    ],
    "http://purl.org/dc/terms/memberOf": [
      {
        "@value": "_:MIV001"
      }
    ]
  },
  {
    "@id": "_:vkmauto001",
    "@type": [
      "https://data.vlaanderen.be/ns/verkeersmetingen#Verkeersmeting"
    ],
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
            "@id": "https://data.vlaanderen.be/doc/conceptscheme/Vkmverkeerskenmerktype/snelheid"
          }
        ],
        "https://data.vlaanderen.be/ns/verkeersmetingen#voertuigType": [
          {
            "@id": "https://data.vlaanderen.be/doc/conceptscheme/VkmVoertuigType/auto"
          }
        ]
      }
    ],
    "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.featureOfInterest": [
      {
        "@id": "_:rst001"
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
        "@value": 0
      }
    ],
    "http://purl.org/dc/terms/memberOf": [
      {
        "@value": "_:MIV001"
      }
    ]
  },
  {
    "@id": "_:vmtauto001",
    "@type": [
      "https://data.vlaanderen.be/ns/verkeersmetingen#Verkeersmeting"
    ],
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
            "@id": "https://data.vlaanderen.be/doc/conceptscheme/Vkmverkeerskenmerktype/aantal"
          }
        ],
        "https://data.vlaanderen.be/ns/verkeersmetingen#voertuigType": [
          {
            "@id": "https://data.vlaanderen.be/doc/conceptscheme/VkmVoertuigType/auto"
          }
        ]
      }
    ],
    "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.featureOfInterest": [
      {
        "@id": "_:wgs426009"
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
        "@value": 0
      }
    ],
    "http://purl.org/dc/terms/memberOf": [
      {
        "@value": "_:MIV001"
      }
    ]
  },
  {
    "@id": "_:fenomtime001",
    "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.phenomenonTime": [
      {
        "@type": [
          "http://www.w3.org/2006/time#ProperInterval"
        ],
        "http://www.w3.org/2006/time#hasBeginning": [
          {
            "@type": [
              "http://www.w3.org/2006/time#Instant"
            ],
            "http://www.w3.org/2006/time#inXSDDateTime": [
              {
                "@type": "xml-schema:dateTime",
                "@value": "20230801T10:10:00+01:00"
              }
            ]
          }
        ],
        "http://www.w3.org/2006/time#hasEnd": [
          {
            "@type": [
              "http://www.w3.org/2006/time#Instant"
            ],
            "http://www.w3.org/2006/time#inXSDDateTime": [
              {
                "@type": "xml-schema:dateTime",
                "@value": "20230801T11:11:12+02:00"
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
        "@type": [
          "http://www.opengis.net/ont/sf#Point"
        ],
        "http://www.opengis.net/ont/geosparql#asGML": [
          {
            "@type": "http://www.opengis.net/ont/geosparql#gmlliteral",
            "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/31370\"><gml:coordinates>144474.5297,208293.5324</gml:coordinates><gml:Point>"
          }
        ]
      }
    ]
  },
  {
    "@id": "_:mti001",
    "@type": [
      "https://www.w3.org/ns/sosa/Sensor"
    ],
    "http://www.w3.org/ns/ssn/implements": [
      {
        "@type": [
          "http://www.w3.org/2004/02/skos/core#Concept"
        ],
        "http://purl.org/dc/terms/type": [
          {
            "@id": "https://data.vlaanderen.be/doc/conceptscheme/VkmObservatieProcedure/type"
          }
        ]
      }
    ],
    "http://purl.org/dc/terms/type": [
      {
        "@id": "https://data.vlaanderen.be/doc/conceptscheme/VkmMeetInstrumentType/verkeersmeting"
      }
    ]
  }
]



´´´
