#Alex Kreimann
#22.10.2024
#Ülesanded07 loendid

import datetime

x=datetime.datetime.now()
tana=int(x.strftime("%m"))-1

"""
#12kuud
kuud=[["jaanuar",7,-15,-1,-4,-16,21,-2,19,6,14,13,14,-3,17,29,6,29,-1,1,27,-6,-10,7,-18,-6,3,-2,12,16,-13,10],
["veebruar",9,-9,-20,2,12,-20,-3,-4,-1,14,-18,-17,24,-11,5,-18,-8,-18,4,-19,13,14,29,11,12,25,-13,9,21,0,-2],
["märts",23,9,3,7,13,28,2,20,-13,21,16,7,14,27,8,15,1,17,-11,23,27,-20,-1,-8,15,-6,-13,10,0,-1,10],
["aprill",19,9,1,30,22,12,-19,-5,-15,-18,4,26,21,-16,15,22,25,-17,-7,15,30,15,-18,-11,20,21,-11,0,-16,17,-8],
["mai",-1,22,-3,29,15,18,-15,20,-10,13,26,7,27,26,6,11,12,-19,26,-8,24,30,28,-18,-6,-20,0,-11,6,-19,11],
["juuni",6,-16,19,-13,-20,-1,15,-18,-1,-5,6,-3,11,-20,28,-16,-4,-18,9,-16,-12,4,-4,-4,-11,8,3,13,7,18,1],
["juuli",-5,4,11,2,-20,27,2,-3,5,-20,-4,21,-15,20,7,-12,3,8,12,-9,30,27,8,12,4,12,30,11,27,15,30],
["august",19,24,-8,-2,14,-1,17,-1,21,15,-5,-20,9,17,3,-2,-8,8,1,-12,27,30,-7,11,7,-2,7,-19,27,-18,-3],
["september",21,-14,30,-15,1,25,-5,20,-12,11,-9,-7,-6,-13,29,8,28,-9,14,13,15,-13,-8,1,29,27,9,4,-19,18,-16],
["oktoober",-1,-1,-5,3,20,-14,-11,12,-14,3,-11,-9,-7,27,-13,22,-12,-16,-19,24,29,27,6,11,-7,14,30,27,9,9,16],
["november",-3,15,-12,-20,-5,0,10,10,20,3,-17,13,17,-5,18,-18,-2,26,7,19,-20,9,-8,15,24,-3,-5,30,-19,11,-3],
["detsember",3,20,-2,15,-10,11,-6,5,7,-8,12,-6,22,24,14,5,21,14,-3,-11,-19,15,-10,-20,7,-1,9,-18,26,17,6]]
"""

"""
#Kommentaar
print(kuud[tana][0])
print(f"Viimane mõõtmine sellel kuul: {kuud[tana][len(kuud[tana])-1]}")
ajutine=[]
for i in range(len(kuud[tana])-1):
    ajutine-append(kuud[tana][i+1])
    print(kuud[tana][i+1],end", ")
print(f"Max temp: {max(ajutine)}")
print(f"Min temp: {min(ajutine)}")
print(f"Keskmine temp: {round(sum(ajutine)/len(ajutine), 2)}")

print(f"-20 esineb {ajutine.count(-20,ajutine)} korda")

ajutine.pop(5)
print(ajutine)
"""

"""
#Kommentaar
muusika=[
'ALIKA – "Bridges"','Anett x Fredi – "Read Between The Lines"','villemdrillem – "leekiv armastus"','Clicherik & Mäx – "PAKSUD"','nublu – "ära ärata"','NOËP – "Move Your Feet"',
'Trad.Attack! – "Bring It On"','Bedwetters – "It Is What It Is"','Reket – "Panama paberid"','Grete Paia – "Võluväel"']

for i in range(len(muusika)):
    print(str(i+1)+". "+muusika[i])
try:
    valik=int(input("v`Vali laul: "))
    print(f"Mängin lugu {muusika[valik-1]}")
except:
    print("Midagi läks katki. Teavita admini!")
"""