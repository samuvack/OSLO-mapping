# Importeer de nodige modules
import requests
from bs4 import BeautifulSoup
from selenium import webdriver  
import requests
import json

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


context_url = "https://raw.githubusercontent.com/samuvack/context/main/wegenregister.jsonld"
response = requests.get(context_url)

data = response.json()

# Geef de url van de website die je wilt scrapen
url = "https://data.vlaanderen.be/doc/applicatieprofiel/wegenregister/"

# Laad de website in de webdriver
driver.get(url)

# Wacht tot de pagina volledig geladen is
driver.implicitly_wait(10)

# Maak een BeautifulSoup object aan met de html broncode van de website
soup = BeautifulSoup(driver.page_source, "html.parser")

# Zoek naar alle tabel row elementen met een id dat "%3A" bevat
rows = soup.find_all("tr", id=lambda x: x and "%3A" in x)

# Maak een lege lijst om de gevonden hrefs op te slaan
hrefs = []
list=[]

# Loop over elke rij
for row in rows:
    d = {}
    
    id = row["id"]
    print(id)
    id = id.replace('%3A', '.')
    list.append(id)
    
    # Zoek naar de tweede td element in de rij
    td = row.find_all("td")[1]
    # Zoek naar het eerste a element in de td element
    a = td.find("a")
    # Haal de href attribuut van het a element op
    href = a["href"]
    # Voeg de href toe aan de lijst

    hrefs.append(href)

lower = [s.replace(' ','').lower() for s in list]

# Define a function that takes a list and an element as parameters
def find_element(list, element):
  # Loop through the list using enumerate to get the index and value of each item
  for index, value in enumerate(list):
    # If the value matches the element, return the index
    if value == element:
      return index
  # If the loop ends without finding the element, return -1 to indicate not found
  return -1


# Print de lijst van hrefs
print(hrefs[0])


# Importeer de json module om de jsonld file te verwerken
import json

"""
# Open de jsonld file en laad de inhoud in een variabele genaamd data
with open("context_url", "r") as f:
  data = json.load(f)
"""

# Haal de waarde van de "@context" sleutel op uit de data
context = data["@context"]

# Ga door elke sleutel en waarde in de context
for key, value in context.items():
  # Als de waarde een dict is, dan is het een eigenschap
  if isinstance(value, dict):
        # Controleer of de dict "@type": "@id" bevat
        if value.get("@type") == "@id":
            # Voeg de eigenschap toe aan de lijst met het formaat "Eigenschap: <key>"
            result = find_element(list, key)
            #print(context[key])
            #print(result)
            if(result>0):
                #print(hrefs[result][key])
                if ('http' in hrefs[result]):
                    context[key]['@type'] = str(hrefs[result])
                else:
                    context[key]['@type'] = 'https://data.vlaanderen.be/doc/applicatieprofiel/verkeersmetingen' + \
                        str(hrefs[result])
            else:
                test = key.replace(' ','').lower()
                result = find_element(lower, test)
                #print(result)
                if ('http' in hrefs[result]):
                    context[key]['@type'] = str(hrefs[result])
                else:
                    print(hrefs[result])
                    context[key]['@type'] = 'https://data.vlaanderen.be/doc/applicatieprofiel/verkeersmetingen' + \
                        str(hrefs[result])
                

#print(context)
data["@context"] = context

# Open the file in write mode
with open('output.jsonld', "w") as f:
    # Write the jsonld object to the file with indent 2
    json.dump(data, f, indent=2)

# Sluit de webdriver
driver.close()
