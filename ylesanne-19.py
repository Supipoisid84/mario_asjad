#Alex Kreimann
#14.01.2025
#Ülesanne19

import json

# Kuva 12.klassi õpilaste nimekiri
# Kuva mitu õpilast õpib 10, 11 ja 12 klassis
# Kuva millistes trennides õpilased käivad
# Kuva 12 klassi õpilaste hinneteleht (nimi, ained, punktid)

import json

# Olemasoleva JSON andmete laadimine
try:
    with open('haridustulemused.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
except FileNotFoundError:
    data = []

print(data)

# Muudetud andmete tagasi faili kirjutamine
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)