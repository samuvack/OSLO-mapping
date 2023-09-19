# Importeer de json module om met JSON bestanden te werken
import json

# Open het JSON-LD bestand in leesmodus en sla het op in een variabele
with open("expanded.jsonld", "r") as f:
    jsonld_data = f.read()

# Converteer de JSON-LD data naar een Python dictionary
jsonld_dict = json.loads(jsonld_data)

# Definieer een functie die de onnodige haakjes verwijdert uit een dictionary

print(type(jsonld_dict))


def remove_brackets(d):
    # Maak een lege dictionary aan om het resultaat op te slaan
    result = {}
    # Loop door alle sleutels en waarden in de dictionary
    for key, value in d.items():
        # Als de waarde een dictionary is, roep de functie recursief aan om de haakjes te verwijderen
        if isinstance(value, dict):
            value = remove_brackets(value)
        # Als de waarde een lijst is, loop door de elementen in de lijst
        elif isinstance(value, list):
            # Maak een lege lijst aan om het resultaat op te slaan
            new_list = []
            # Loop door de elementen in de lijst
            for item in value:
                # Als het element een dictionary is, roep de functie recursief aan om de haakjes te verwijderen
                if isinstance(item, dict):
                    item = remove_brackets(item)
                # Voeg het element toe aan de nieuwe lijst
                new_list.append(item)
            # Vervang de waarde door de nieuwe lijst
            value = new_list
        # Voeg de sleutel en waarde toe aan de resultaat dictionary
        result[key] = value
    # Geef de resultaat dictionary terug
    return result


# Roep de functie aan op de JSON-LD dictionary en sla het resultaat op in een variabele
new_jsonld_dict = remove_brackets(jsonld_dict)

# Converteer het resultaat terug naar een JSON-LD data string
new_jsonld_data = json.dumps(new_jsonld_dict)

# Open een nieuw bestand in schrijfmodus en schrijf het resultaat erin
with open("new_jsonld_file.json", "w") as f:
    f.write(new_jsonld_data)
