---
sort: 5
---

# Signco

```note
Deze OSLO mapping heeft nog GEEN cross check ondergaan, er kunnen nog wijzigingen gebeuren na cross check. Het vereenvoudigd implementatiemodel (overview figuur) wordt later nog gefinaliseerd.
```

## Vereenvoudigd implementatie model

<div id="enlargeImage">
<a href="https://raw.githubusercontent.com/samuvack/Implementatie-OSLO-mapping/main/images/Fietstellus_overview.jpg"><img src="../images/Fietstellus_overview.jpg" width="100%" text-align="center"></a>
</div>



## Data input


```json
{
 "data": [
 {
 "address": {
 "line1": "Jozef de Blockstraat 74",
 "zipCode": "2830",
 "city": "Willebroek",
 "country": "Belgium"
 },
 "coordinate": {
 "latitude": 51.041935,
 "longitude": 4.35714
 },
 "measuringPoints": [
 {
 "guid": "eb58f640-6916-4986-8ded-c7bf5a0fc40d",
 "code": "Willebroek South In",
 "description": "Opposite the buildings",
 "heading": 30,
 "from": "Tisselt",
 "to": "Willebroek",
 "drivingLane": "Single lane",
 "analysisTypeId": "car"
 },
 {
 "guid": "ff88e990-5a66-4301-a2cd-e75c897b48a8",
 "code": "Willebroek South Out",
 "heading": 210,
 "from": "Willebroek",
 "to": "Tisselt",
 "drivingLane": "Single lane",
 "analysisTypeId": "car"
 }
 ]
 }
 ]
}

```


```json
{
    "@context": [
        "https://data.vlaanderen.be/doc/applicatieprofiel/verkeersmetingen/ontwerpstandaard/2023-03-14/context/Verkeersmetingen-ap.jsonld",
        "https://data.vlaanderen.be/doc/applicatieprofiel/sensoren-en-bemonstering/kandidaatstandaard/2022-04-28/context/ap-sensoren-en-bemonstering.jsonld",
        "https://data.vlaanderen.be/doc/applicatieprofiel/observaties-en-metingen/kandidaatstandaard/2022-04-28/context/ap-observaties-en-metingen.jsonld",
        "https://raw.githubusercontent.com/samuvack/context/main/wegenregister.jsonld",
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
            "adms": "http://www.w3.org/ns/adms#",

            "cl-vrt":"https://data.vlaanderen.be/doc/conceptscheme/VkmVoertuigTypes",
            "cl-vkt": "https://data.vlaanderen.be/doc/conceptscheme/Vkmverkeerskenmerktype",
            "cl-trt" : "https://inspire.ec.europa.eu/codelist/LinkDirectionValue",
            "cl-mit": "https://data.vlaanderen.be/doc/conceptscheme/VkmMeetInstrumentType",
            "cl-op": "https://data.vlaanderen.be/doc/conceptscheme/VkmObservatieProcedure",
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
                "Netwerkreferentie.element": "_:wgs001",
                "Linkreferentie.toepassingsRichting": "cl-trt:gelijklopend"
            },
            "Rijrichting.rijrichting": "cl-trt:gelijklopend"
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
            "@id":"_:wgs001",
            "@type":"Wegsegment",
            "Wegsegment.beginknoop":"_:wgkn001",
            "Wegsegment.eindknoop":"_:wgkn002"
        },
        {
            "@id": "_:wgkn001",
            "@type": "Wegknoop",
            "Wegknoop.geometrie": {
                "@type": "Punt",
                "Geometrie.gml": {
                    "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/4326\"><gml:coordinates></gml:coordinates><gml:Point>",
                    "@type": "geosparql:gmlliteral"
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
                    "@type": "geosparql:gmlliteral"
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
            "Observatie.fenomeentijd":":_fenomtime001",
            "Verkeersmeting.resultaat": 30,
            "Observatie.uitgevoerdDoor": "_:mti001",
            "Verkeersmeetpunt":"_:mpt001",
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
            "Observatie.fenomeentijd":":_fenomtime001",
            "Verkeersmeting.resultaat": 210,
            "Observatie.uitgevoerdDoor": "_:mti001",
            "Verkeersmeetpunt":"_:mpt001",
            "dct:memberOf": "_:Signco001"
        },
        {
        "@id":"_:fenomtime001",
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
                "@id":"_:mpt001", 
                "@type": "Verkeersmeetpunt",
                "Bemonsteringspunt.geometrie": {
                        "@type": "Punt",
                        "Geometrie.gml": {
                            "@value": "<gml:Point srsName=\"http:\\//www.opengis.net/def/crs/EPSG/0/4326\"><gml:coordinates>51.041935,4.35714</gml:coordinates><gml:Point>",
                            "@type": "geosparql:gmlliteral"
                        }
                    },
               
                "Verkeersmeetpunt.rijstrook":"_rst001"},
        
        {
            "@id": "_:mti001",
            "@type": "Sensor",
            "Systeem.type": "cl-mit:atc",
            "Sensor.implementeert":{
                "@type":"Observatieproceduretype",
                "Observatieprocedure.type":"cl-op:type"}

        }

    ]
}


```
