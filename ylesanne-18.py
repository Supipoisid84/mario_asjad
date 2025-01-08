#Alex Kreimann
#08.01.2025
#Kikas01

import csv

# Lae andmed alla ja lahenda järgmised probleemid (iga punkt eraldi lahendus):

#     Kuva mitu meeskonda osales ja too välja nimekiri (täpitähed peavad korras olema ja jälgi, et esimese rea jätad vahele)
#     Leia mitu mängu igal meeskonnal oli (kasuta sõnastikku, kui meeskond on juba sõnastikus, siis suurendad selle väärtust +1)
#     Leia iga meeskonna võidud ja kaotused ning kirjuta tulemused uude Exceli sõbralikku CSV faili

faili_nimi = 'EstonianBasketballGames.csv'

meeskonnad=[]
mangud={}

# Faili avamine ja lugemine
with open(faili_nimi, mode='r', encoding='utf-8') as fail:
    csv_lugeja = csv.reader(fail)
   
    pais = next(csv_lugeja) 
    
    for rida in csv_lugeja:
        mk=rida[1]
        mk2=rida[2]
        if mk not in meeskonnad:
            meeskonnad.append(mk)
        if mk not in mangud:
            mangud[mk]=1
        else:
            mangud[mk]+=1
        if mk2 not in mangud:
            mangud[mk2]=1
        else:
            mangud[mk2]+=1

print(f"osales {len(meeskonnad)} meeskonda")

uusfail = 'mangud.csv'

with open(uusfail, mode='w', newline='', encoding='utf-8') as fail:
    csv_fail = csv.writer(fail, delimiter=';')  # Semikoolon veerueraldajana
   
    for key,value in mangud.items():
       csv_fail.writerow([key.encode('utf-8'),value])