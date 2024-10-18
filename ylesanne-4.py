#Alex Kreimann
#16.10.2024
#Ülesanded04

import turtle

#5. Ringi pindala ja Turtle
try:
    r=int(input("Lisa ringi raadius: "))
    pi=3.14
    s=pi*r**2
    p=2*pi*r
    print(f"Ringi pindala on {s:.2f} ja ümbermõõt on {p:.2f}")
    turtle.circle(r,360)
except:
    print("Tegid sisestamisel vea!") 
#4. Kingituste pakkimine
try:
    kingitused=int(input("Lisa kinkide arv: "))
    maht=5
    pakid=kingitused//maht
    üle=kingitused%maht
    print(f"Saad teha{pakid} täis kinkekasti. Üle jääb {üle} kingitust")
except:
    print("Tegid sisestamisel vea!")

#3. Faili allalaadimine
try:
    failiSuurus=int(input("Sisesta faili suurus (MB): "))
    downKiirus=int(input("Sisesta allalaadimise kiirus (MB(s)): "))
    aeg=failiSuurus/downKiirus
    print(f"Allalaadimiseks kulub {aeg:0.2f} sekundit")
except:
    print("Tegid sisestamisel vea!")

#2. Raamatute allahindlus
ale=0.3
arv=3
hind=12.53
summa=hind-(hind*ale)*arv
print(f"{arv} raamatu hind soodustusega on {summa:0.2f}€")

#1. Aia pikkus
a=(input("Sisesta külg 1: "))
b=(input("Sisesta külg 2: "))
p=2*(2+b)
print(f"Aia kogupikkus on {p} meetrit")

turtle.done