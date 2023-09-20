---
layout: default
parent: Geomobility
title: expanded OSLO mapping
nav_order: 5
---

# expanded OSLO mapping

```json
[
  {
    "@id": "_:GM001",
    "@type": "http://www.w3.org/ns/dcat#Dataset",
    "http://purl.org/dc/terms/description": {
      "@language": "nl",
      "@value": "Floating Car Data geeft een zeer goed beeld van de verkeerssituatie in een stad, maar soms is het essentieel om exact te weten hoeveel verkeer er in bothDirections richtingen door een straat rijdt en wat de modal split is."
    },
    "http://purl.org/dc/terms/title": {
      "@language": "nl",
      "@value": "GeoMobility."
    },
    "http://purl.org/dc/terms/accessRights": "http://publications.europa.eu/resource/authority/access-right/PUBLIC",
    "http://www.w3.org/ns/dcat#keyword": {
      "@language": "nl",
      "@value": "GeoMobility"
    }
  },
  {
    "@id": "_:rri001",
    "@type": "https://data.vlaanderen.be/ns/weg#Rijrichting",
    "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.result": {
      "@type": "https://data.vlaanderen.be/ns/netwerk/#Linkreferentie",
      "https://data.vlaanderen.be/ns/netwerk/#toepassingsRichting": "https://inspire.ec.europa.eu/codelist/LinkDirectionValue/inDirection",
      "https://data.vlaanderen.be/ns/weg#NetwerkElement": "_:wgs001"
    },
    "https://data.vlaanderen.be/ns/weg#rijrichting": "https://inspire.ec.europa.eu/codelist/LinkDirectionValue/inDirection"
  },
  {
    "@id": "_:wgs001",
    "@type": "https://data.vlaanderen.be/ns/weg#Wegsegment",
    "https://data.vlaanderen.be/ns/netwerk/#beginknoop": "_:wgkn001",
    "https://data.vlaanderen.be/ns/netwerk#eindknoop": "_:wgkn002",
    "https://data.vlaanderen.be/ns/weg#middellijnGeometrie": {
      "@type": "LineString",
      "http://www.opengis.net/ont/geosparql#asWKT": {
        "@type": "http://www.opengis.net/ont/geosparql#wktLiteral",
        "@value": "<http://www.opengis.net/def/crs/EPSG/0/4326> LINESTRING (30 10, 10 30, 40 40)"
      }
    }
  },
  {
    "@id": "_:wgkn001",
    "@type": "https://data.vlaanderen.be/ns/weg#Wegknoop",
    "https://data.vlaanderen.be/ns/weg#geometrie": {
      "@type": "http://www.opengis.net/ont/sf#Point",
      "http://www.opengis.net/ont/geosparql#asGML": {
        "@type": "http://www.opengis.net/ont/geosparql#gmlLiteral",
        "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/4326\"><gml:coordinates> 3.24239104986191, 51.2259355430829</gml:coordinates><gml:Point>"
      }
    }
  },
  {
    "@id": "_:wgkn002",
    "@type": "https://data.vlaanderen.be/ns/weg#Wegknoop",
    "https://data.vlaanderen.be/ns/weg#geometrie": {
      "@type": "http://www.opengis.net/ont/sf#Point",
      "http://www.opengis.net/ont/geosparql#asGML": {
        "@type": "http://www.opengis.net/ont/geosparql#gmlLiteral",
        "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/4326\"><gml:coordinates>3.24177950620651, 51.2256331896095</gml:coordinates><gml:Point>"
      }
    }
  },
  {
    "@id": "_:vkmauto001",
    "@type": "https://data.vlaanderen.be/ns/verkeersmetingen#Verkeersmeting",
    "https://def.isotc211.org/iso19156/2011/Observation#OM_Observation.phenomenonTime": ":_fenomtime001",
    "https://data.vlaanderen.be/ns/verkeersmetingen#geobserveerdKenmerk": {
      "@type": "https://data.vlaanderen.be/ns/verkeersmetingen#Verkeerskenmerk",
      "https://data.vlaanderen.be/ns/verkeersmetingen#type": "https://data.vlaanderen.be/doc/concept/VkmVerkeersKenmerkType/aantal",
      "https://data.vlaanderen.be/ns/verkeersmetingen#voertuigType": "https://data.vlaanderen.be/doc/concept/VkmVoertuigType/fiets"
    },
    "https://data.vlaanderen.be/ns/verkeersmetingen#geobserveerdObject": "_:mpt001",
    "http://def.isotc211.org/iso19156/2011/Observation#OM_Observation.result": {
      "@type": "http://def.isotc211.org/iso19103/2005/RecordsAndClassMetadata#Any",
      "@value": 5
    },
    "https://data.vlaanderen.be/ns/observaties-en-metingen/#Observatie.uitgevoerdDoor": "_:mti001",
    "http://purl.org/dc/terms/memberOf": {
      "@value": "_:GM001"
    }
  },
  {
    "@id": "_:fenomtime001",
    "https://def.isotc211.org/iso19156/2011/Observation#OM_Observation.phenomenonTime": {
      "@type": "http://www.w3.org/2006/time#ProperInterval",
      "http://www.w3.org/2006/time#hasBeginning": {
        "@type": "http://www.w3.org/2006/time#Instant",
        "http://www.w3.org/2006/time#inXSDDateTime": {
          "@type": "xml-schema:dateTime",
          "@value": "20161122T09:00:00.000Z"
        }
      },
      "http://www.w3.org/2006/time#hasEnd": {
        "@type": "http://www.w3.org/2006/time#Instant",
        "http://www.w3.org/2006/time#inXSDDateTime": {
          "@type": "xml-schema:dateTime",
          "@value": "20161122T10:00:00.000Z"
        }
      }
    }
  },
  {
    "@id": "_:mpt001",
    "@type": "https://data.vlaanderen.be/ns/verkeersmetingen#Verkeersmeetpunt",
    "https://data.vlaanderen.be/ns/verkeersmetingen#bemonsterdObject": "_:rri001",
    "https://data.vlaanderen.be/ns/weg#geometrie": {
      "@type": "http://www.opengis.net/ont/sf#Point",
      "http://www.opengis.net/ont/geosparql#asGML": {
        "@type": "http://www.opengis.net/ont/geosparql#gmlLiteral",
        "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/4326\"><gml:coordinates>3.24177950620651, 51.2256331896095</gml:coordinates><gml:Point>"
      }
    },
    "https://data.vlaanderen.be/ns/verkeersmetingen#netwerkreferentie": "_:pr001"
  },
  {
    "@id": "_:pr001",
    "@type": "https://data.vlaanderen.be/ns/netwerk/#Puntreferentie",
    "https://data.vlaanderen.be/ns/netwerk/#toepassingsRichting": "https://inspire.ec.europa.eu/codelist/LinkDirectionValue/bothDirections",
    "https://data.vlaanderen.be/ns/netwerk/#opPositie": {
      "@type": "https://schema.org/Distance",
      "https://schema.org/unitCode": {
        "@type": "https://w3id.org/cdt/ucumunit",
        "@value": "m"
      },
      "https://schema.org/value": "300"
    }
  },
  {
    "@id": "_:mti001",
    "@type": "https://www.w3.org/ns/sosa/Sensor",
    "http://www.w3.org/ns/ssn/implements": {
      "@type": "http://www.w3.org/2004/02/skos/core#Concept",
      "http://purl.org/dc/terms/type": "cl-opt:type"
    },
    "http://purl.org/dc/terms/type": "https://data.vlaanderen.be/doc/concept/VkmMeetInstrumentType/rubberslang"
  }
]
```
