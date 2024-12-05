#Alex Kreimann
#20.11.2024
#Ülesanne16

import os
import datetime

nimi=os.getlogin()
print(f"Tere {nimi}!")

print(f"Sa oled: {os.getcwd()}")

kokku=3
x=datetime.datetime.now().strftime('%Y%m&d')
try:
    for i in range(kokku):
        kataloog=x+"_"+str(i+1)
        os.mkdir(kataloog)
        print(kataloog)
except:
    print("Sul on juba need kataloogid!")

valik=input("Lisa kataloog, mida kustudada: ")
try:
    os.rmdir(valik)
    print(valik+" kustutatud")
except:
    print("Tõrge tekkis kustutamisel!")

print(os.listdir())