# Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
openai.api_type = "azure"
openai.api_base = "https://oslo-mapping.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = "ece4aaf842004666889e51749f41f3a7"

prompt = """Convert a data set from the format JSON file into OSLO (Open Standard for Linked Organisations) compliant JSON-LD file. Ensure the correct context is added based on the existing OSLO standards.Input JSON file 1:{ \"1-Aalst Station\" : {\"Locatie\" : {\"CRS\" : \"EPSG:31370\",\"Geometrie\" : \"POLYGON ((126966 181444,...))\"},\"Attributen\" : {\"ID\" : \"1\",\"Naam\" : \"Aalst Station\",\"Provincie\" : \"Oost-Vlaanderen\",\"VVR\" : \"Aalst\",\"Gemeente\" : \"Aalst\",\"Status\" : \"Goedgekeurd\",\"Categorie BVR\" : \"Interregionaal\",\"Beheer\" : [ \"Lokaal bestuur\" ],\"Mobiliteitsaanbod\" : {\"Deelsystemen\" : [{\"Naam\" : \"VOM deelmobiliteit\",\"Aanbod\" : [ \"Deelwagens, Deelfietsen\" ]}],\"Lijnbus halte\" : \"false\",\"Tramhalte\" : \"false\",\"Kernnet\" : \"true\",\"Aanvullend net\" : \"true\",\"Functioneel net\" : \"true\",\"Metrohalte\" : \"false\",\"Treinstation\" : \"false\",\"VOM flex halte\" : \"false\",\"Deelwagen VOM\" : \"false\",\"Deelfiets VOM\" : \"false\",\"Fietslockers\" : \"false\",\"Deelsteps\" : \"false\",\"Fietspomp\" : \"false\",\"Park and ride\" : \"false\",\"Kiss and ride\" : \"false\", \"Fietsenstalling\": [{\"Overdekt\": \"true\",\"Beveiligd\": \"true\",\"Toegankelijk buitenmaatse fietsen\": \"true\"}],\"Aantal laadpunten EV\": \"1\",\"Aantal laadpunten E-bike\": \"0\",\"Aantal parkeerplaatsen carpool\": \"0\",\"Aantal parkeerplaatsen wagens\": \"0\",\"Aantal parkeerplaatsen beperking\": \"0\",\"Aantal laadpunten EV deelwagens buiten VOM\": \"0\",\"Aantal parkeerplaatsen deelwagens buiten VOM\": \"0\",\"Aantal laadpunten E-bike deelfietsen buiten VOM\": \"0\"},\"Aanvullend aanbod\" : {\"Wachtaccomodatie\" : \"true\",\"Vuilnisbak\" : \"false\",\"Pakketautomaat\" : \"false\",\"Bagagelocker\" : \"false\",\"Fietshersteldienst\" : \"false\",\"Sanitair\" : \"false\",\"Rode brievenbus\" : \"false\",\"AED\" : \"false\",\"Geld automaat\" : \"false\",\"Wifi\" : \"false\",\"Oplaadpunt smartphones\" : \"false\",\"Drinkerwatervoorziening\" : \"false\",\"Vergaderruimte\" : \"false\",\"Voedings-en krantenwinkel\" : \"false\",\"Eet- en drankgelegenheid\" : \"false\",\"Uitleenpunt kinderwagens\" : \"false\",\"Spin-off centrumdiensten\" : \"false\"}}}}Output JSON-LD file 1:{{\"@context\": [\"https://data.vlaanderen.be/doc/applicatieprofiel/mobiliteit/vervoersknooppunten/erkendestandaard/2022-12-01/context/OSLO-Vervoersknooppunten-ap.jsonld\",\"https://data.vlaanderen.be/doc/applicatieprofiel/infrastructuurelementen/erkendestandaard/2021-09-30/context/infrastructuurelementen-ap.jsonld\",\"https://data.vlaanderen.be/doc/applicatieprofiel/generiek-basis/zonderstatus/2019-07-01/context/generiek-basis.jsonld\",\"https://raw.githubusercontent.com/GeertThijs/MyFiles/master/ContextfileOrganisatie.jsonld\",\"https://data.vlaanderen.be/context/adresregister.jsonld\",{\"Polygon\": \"http://www.opengis.net/ont/eo-geojson/1.0/\",\"dcterms\": \"http://purl.org/dc/terms/\",\"rdf\": \"http://www.w3.org/1999/02/22-rdf-syntax-ns#\",\"geosparql\": \"http://www.opengis.net/ont/geosparql#\",\"locn\": \"http://www.w3.org/ns/locn#\",\"adres\": \"https://data.vlaanderen.be/ns/adres#\",\"time\": \"http://www.w3.org/2006/time#\",\"xml-schema\": \"http://www.w3.org/2001/XMLSchema#\",\"skos\": \"http://www.w3.org/2004/02/skos/core#\",\"NetwerkElement.netwerk\": {\"@reverse\": \"https://data.vlaanderen.be/ns/netwerk#bestaatUit\"},\"cl-idt\": \"https://example.com/concept/identificatortype/\",\"cl-plt\": \"https://example.com/concept/plaatstype/\",\"cl-hcl\": \"https://example.com/concept/hoppinpuntclassificatie/\",\"cl-hst\": \"https://example.com/concept/hoppinpuntstatus/\",\"cl-mdt\": \"https://example.com/concept/mobiliteitsdiensttype/\",\"cl-tkt\": \"https://example.com/concept/transportknooptype/\",\"cl-trt\": \"https://example.com/concept/transporttype/\",\"cl-avd\": \"https://example.com/concept/aanvullendedienst/\",\"cl-ine\": \"https://example.com/concept/infrastructuurelement/\",\"cl-vm\": \"https://example.com/concept/vervoersmiddel/\"}],\"@graph\": [{\"@id\": \"_:vkn001\",\"@type\": \"Hoppinpunt\",\"GeregistreerdVervoersknooppunt.registratie\": {\"@type\": \"Identificator\",\"Identificator.identificator\": {\"@value\": \"1\",\"@type\": \"cl-idt:hoppinpunt\"}},\"Vervoersknooppunt.naam\": {\"@value\": \"Station Aalst\",\"@language\": \"nl\"},\"Vervoersknooppunt.locatie\": [{\"@type\": \"Plaats\",\"Plaats.plaatsnaam\": {\"@value\": \"Aalst\",\"@language\": \"nl\"},\"dcterms:type\": \"cl-plt:vervoersregio\"},{\"@type\": \"Plaats\",\"Plaats.plaatsnaam\": {\"@value\": \"Aalst\",\"@language\": \"nl\"},\"dcterms:type\": \"cl-plt:gemeente\"},{\"@type\": \"Polygon\",\"Geometrie.gml\": {\"@value\": \"<gml:Polygon srsName=\\"http: \\// www.opengis.net/def / crs/EPSG/0/31370\\"><gml:coordinates>126966 181444,126958.387953251 181405.731656763,126936.710678119 181373.289321881,126904.268343237 181351.612046749,126866 181344,126827.731656763 181351.612046749,126795.289321881 181373.289321881,126773.612046749 181405.731656763,126766 181444,126773.612046749 181482.268343236,126795.289321881 181514.710678119,126827.731656763 181536.387953251,126866 181544,126904.268343237 181536.387953251,126936.710678119 181514.710678119,126958.387953251 181482.268343236,126966 181444</gml:coordinates><gml:Polygon>\",\"@type\": \"geosparql:gmlliteral\"}}],\"Vervoersknooppunt.classificatie\": \"cl-hcl:interregionaal\",\"Vervoersknooppunt.status\": [\"cl-hst:goedgekeurd\"],\"Vervoersknooppunt.wegbeheerder\": {\"@type\": \"Organisatie\",\"voorkeursnaam\": {\"@value\": \"Aalst\",\"@language\": \"nl\"}},\"Vervoersknooppunt.transportobject\": {\"@type\": \"Transportknoop\",\"Transportknoop.type\": \"cl-tkt:treinstation\",\"Transportknoop.geometrie\": \"<gml:Point srsName=\\"http: \\// www.opengis.net/def / crs/EPSG/0/31370\\"><gml:coordinates>0 0</gml:coordinates><gml:Point>\",\"NetwerkElement.netwerk\": [{\"@type\": \"Transportnetwerk\",\"Transportnetwerk.geografischeNaam\": {\"@value\": \"KernNet\",\"@language\": \"nl\"}},{\"@type\": \"Transportnetwerk\",\"Transportnetwerk.geografischeNaam\": {\"@value\": \"AanvullendNet\",\"@language\": \"nl\"}},{\"@type\": \"Transportnetwerk\",\"Transportnetwerk.geografischeNaam\": {\"@value\": \"FunctioneelNet\",\"@language\": \"nl\"}}]},\"Vervoersknooppunt.dienst\": [\"_:av001\"],\"Vervoersknooppunt.infrastructuurelement\": [\"_:laderEV001\",\"_:fietsstalling001\",\"_:hoppinzuil010\"],\"Vervoersknooppunt.toegankelijkheid\": [{\"@type\": \"Toegankelijkheid\",\"Toegankelijkheid.niveau\": \"cl-tni:zelfstandigToegankelijk\",\"Toegankelijkheid.onderdeel\": \"cl-ton:lift\",\"Toegankelijkheid.type\": \"cl-tty:motorischeBeperking\"},{\"@type\": \"Toegankelijkheid\"}]},{\"@id\": \"_:dienst001\",\"@type\": \"Mobiliteitsdienst\",\"Mobiliteitsdienst.naam\": {\"@value\": \"Deelwagen\",\"@language\": \"nl\"},\"Mobiliteitsdienst.type\": \"cl-mdt:deelwagen\",\"Mobiliteitsdienst.aanbieder\": \"_:organisatie001\",\"Mobiliteitsdienst.uitgevoerdDoor\": \"_:organisatie001\"},{\"@id\": \"_:fietsstalling001\",\"@type\": \"Fietsstalling\",\"Parkeerfaciliteit.capaciteit\": {\"@type\": \"Capaciteit\",\"Capaciteit.maximum\": 5,\"Capaciteit.totaal\": 20,\"Capaciteit.voertuigtype\": {\"@value\": \"fiets\",\"@type\": \"cl-vrtgtype:fiets\"}},\"Parkeerfaciliteit.openingsuren\": {\"@type\": \"Periode\",\"Periode.begin\": {\"@type\": \"time:Instant\",\"time:inXSDDateTime\": {\"@type\": \"xsd:dateTime\",\"@value\": \"2018-07-06\"}},\"Periode.einde\": {\"@type\": \"time:Instant\",\"time:inXSDDateTime\": {\"@type\": \"xsd:dateTime\",\"@value\": \"2018-07-06\"}}},\"Fietsstalling.overdekt\": \"True\",\"Fietsstalling.afsluitbaar\": \"True\",\"Fietsstalling.fietsdelen\": \"False\",\"Parkeerfaciliteit.kenmerk\": [\"cl-pfk:buitenmaatse_fietsen\"]},{\"@id\": \"_:hoppinzuil010\",\"@type\": \"Hoppinzuil\",\"Hoppinzuil.zuilnaam\": \"Hoppinzuil Aalst\",\"Hoppinzuil.zuilnummer\": \"10\",\"Infrastructuurelement.geometrie\": {\"@type\": \"Punt\",\"Geometrie.gml\": {\"@value\": \"<gml:Point srsName=\\"http: \\// www.opengis.net/def / crs/EPSG/0/31370\\"><gml:coordinates>156579.64 216540.27</gml:coordinates><gml:Point>\",\"@type\": \"geosparql:gmlliteral\"}}},{\"@id\": \"_:laderEV001\",\"@type\": \"Lader\",\"Lader.type\": \"snellader\",\"Lader.vervoermiddel\": \"cl-vm:auto\",\"rdfs:value\": 1},{\"@id\": \"_:av001\",\"@type\": \"AanvullendeDienst\",\"AanvullendeDienst.aanbieder\": \"_:aan099\",\"AanvullendeDienst.naam\": {\"@value\": \"Zitbanken wachtzaal\",\"@language\": \"nl\"},\"AanvullendeDienst.type\": \"cl-avd:wachtacommodatie\",\"AanvullendeDienst.beschikbaarOpInfrastructuurelement\": [{\"@type\": \"Zitbank\"}],\"rdfs:value\": 10},{\"@id\": \"_:organisatie001\",\"@type\": [\"GeregistreerdeOrganisatie\",\"Aanbieder\",\"Uitvoerder\"],\"Organisatie.contactinfo\": {\"@type\": \"Contactinfo\",\"Contactinfo.adres\": {\"@type\": \"Adresvoorstelling\",\"gemeentenaam\": {\"@value\": \"Gent\",\"@language\": \"nl\"},\"straatnaam\": {\"@value\": \"Koningin Maria Hendrikaplein\",\"@language\": \"nl\"},\"huisnummer\": \"65\",\"busnummer\": \"b\",\"postcode\": \"9000\"},\"Contactinfo.telefoon\": \"093884565\"},\"homepage\": \"www.cambio.be\",\"logo\": \"https://cambio.png\",\"registratie\": {\"@type\": \"Identificator\",\"Identificator.identificator\": {\"@value\": \"0479.561.664\",\"@type\": \"cl-idt:kbonummer\"}},\"voorkeursnaam\": {\"@value\": \"Cambio Vlaanderen\",\"@language\": \"nl\"}}]}}Input JSON file2:{{  \"status_code\": 200,  \"message\": \"ok\",  \"type\": \"FeatureCollection\",  \"features\": [    {      \"type\": \"Feature\",      \"geometry\": {\"type\": \"MultiLineString\",\"coordinates\": [  [    [      4.04451041920408,      50.9346197016993    ],    [      4.04468516398887,      50.9346499094883    ],    [      4.04476128017613,      50.9346736897766    ],    [      4.04486091154096,      50.9347048165154    ],    [      4.0450104190652,      50.9347897018035    ],    [      4.04508041942127,      50.9348297017355    ],    [      4.04536795581668,      50.9349798325647    ],    [      4.04561050090522,      50.9350979049717    ],    [      4.04563353497237,      50.9351073291995    ],    [      4.04581042002322,      50.9351797011571    ]  ]]      },      \"properties\": {\"segment_id\": 426009,\"last_data_package\": \"2021-09-30 08:14:03.339300+00:00\",\"timezone\": \"Europe/Brussels\",\"date\": \"2021-09-30 06:00:00+00:00\",\"period\": \"hourly\",\"uptime\": 0.750277777777778,\"heavy\": 26.6567937800814,\"car\": 277.230655312846,\"bike\": 33.3209922251018,\"pedestrian\": 3.99851906701222 }}]}} Output JSON-LD file2:"""


response = openai.Completion.create(engine="GPT4-32k", prompt=prompt, temperature=0,
                                    max_tokens=3802, top_p=1, frequency_penalty=0, presence_penalty=0, stop=None)
print(response)
