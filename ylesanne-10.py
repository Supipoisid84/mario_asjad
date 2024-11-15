#Alex Kreimann
#08.11.2024
#Ülesanne10

import random

katsed=[]
loop=1
arvamused=0
suv=random.randint(1,10)
print(suv)

while loop==1:
    arva= int(input("Arva arv 1-10: "))
    arvamused+=1
    if arva==suv:
        print("Õige")
        print(f"Proovimisi {arvamused} korda!")
        katsed.append(arvamused)
        uuesti=input("Soovid uuesti? (j/e): ")
        if uuesti=="j":
            suv=random.randint(1,10)
            arvamused=0
        else:
            break
    else:
        print("Proovi uuesti")
print("Game Over")
print(arvamused)
