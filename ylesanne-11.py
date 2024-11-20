#Alex Kreimann
#08.11.2024
#Ülesanne11

import turtle
import random

"""
def pikim_sona(*sonad):
    pikim=0
    for i in sonad:
        if len(1)>pikim:
            pikim=len(i)
    print(f"Pikim sõna on {pikim} märki!")

pikim_sona("üks","kaks","kolmkümmend")
"""

"""
def kolm_pikimat_sona(a):
    sonastik={}
    for i in a:
        sonastik[i]=len(i)
    print(sorted(sonastik.items(),key=lambda x:x[1],reverse=True))
for j in range(3):
    print(sorteeritud[j])

sonad=["üks","kaks","viis","kolmsada","üksmiljonsadamust"]
kolm_pikimat_sona(sonad)
"""

"""
def sarnased_esitahed(nimi):
    tykk=nimi.split(" ")
    if tykk[0][0]==tykk[1][0]:
        return True
    return tykk[1][0]

print(sarnased_esitahed("Vapper Vares"))
print(sarnased_esitahed("Lahe Känguru"))
"""

def viisnurk(k):
    pass
def ring(k):
    pass

def ruut(k):
    turtle.speed(0)
    for j in range(k):
        turtle.penup()
        turtle.goto(random.randint(-400,400),random.randint(-400,400))
        turtle.pendown()
        turtle.rt(random.randint(0,90))
        for i in range(4):
            turtle.forward(100)
            turtle.left(90)
def suvaline(k):
    for i in range(k):
        random.choice([viisnurk(1),ring(1),ruut(1)])

print("----------Minu rõve programm----------")
valik=int(input("1 - viisnurk\n2 - ring \n3 - ruut\n4 - suvaline\nLisa valik (1-4): "))
kujunditeArv=int(input("Mitu kujundit soovid joonistada: "))
if valik==1:
    viisnurk(kujunditeArv)
elif valik==2:
    ring(kujunditeArv)
elif valik==3:
    ruut(kujunditeArv)
else:
    suvaline(0)

turtle.done()