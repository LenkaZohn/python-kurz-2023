
import json
with open('body.json', encoding="utf-8") as vstupni_soubor:
    data = json.load(vstupni_soubor)

print(data)
