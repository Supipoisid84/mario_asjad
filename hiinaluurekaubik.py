#Alex Kreimann
#12.12.2024
#Kontrolltöö 7 15 6 2 16

import math

#1. Korrutamise kontrollimine
#	programm esitab korrutustehte 1p
#	ootab kasutajalt vastuse sisestamist 1p
#	kontrollib vastuse Ãµigsust 1p
#	vÃ¤ljastab, kas vastus oli Ãµige vÃµi vÃ¤Ã¤r. 1p
#	kokku antakse lahendamiseks 10 Ã¼lesannet. 1p
	
#2.+ Vanused
#	loo vanuste loend 1p
#	leia numbrite suurim ja vÃ¤ikseim arv  1p
#	kogusumma  1p
#	keskmine 1p
"""
#Ei tööta kurat, sitt kood
#Edit: Nüüd töötab pärast faili nime muutmist, täidab kõiki eesmärke.
vanusteloend=[8,17,69,420,14,84,7,57]
suurimarv=(max(vanusteloend))
väikseimarv=(min(vanusteloend))
kogusumma=sum(vanusteloend)
keskmine=kogusumma/len(vanusteloend)
print("Suurimarv on: ", (suurimarv))
print("Väikseim arv on: ", (väikseimarv))
print("Summa on: ", (kogusumma))
print("Keskmine on:", (keskmine))
"""
#3. Positiivsed ja negatiivsed
#	tee kaks loendit positiivsete ja negatiivsete arvude hoidmiseks 1p
#	kasutaja sisestab 5 arvu ja programm tuvastab, kumba loendisse selle lisab 2p
#	nulli lisamisel ei tehta midagi 1p
#	vÃ¤ljasta mÃµlemad loendit 1p
	
#4. List Less Than Ten
#	Take a list and write a program that prints out all the elements of the list that are less than 5. 1p
#		a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#	Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list. 1p
#	Write this in one line of Python. 1p
#	Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user. 1p
	
#5. Shopping List
#	Create a program that will keep track of items for a shopping list. The program should keep asking for new items until nothing is entered (no input followed by enter/return key). The program should then display the full shopping list.

#6.+ Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris vÃµi paaritu
#	kuvatakse korrektne arusaadav kÃ¼simus ja vastus - 1p
#	eelnev kontroll, kas kasutaja ei lisanud arvu vÃµi pani nulli - 1p
#	kood mis teavitab paaris vÃµi paaritust arvust - 1p
#	kuvatakse programmi pealkiri - 1p
#	kood kommenteeritud - 1p

#Palun 5+ või kingi 6 liitrit kalja. Ma vihkan seda rämpsu, teine punkt sinu nõudmistel ajab närvid läbi.
print("Paaritu arvu kontrollija")
arv=int(input("Sisesta arv: "))
if (arv%2)==0:
    print("Arv on paaris.")
elif arv==" ":
    print("Ei")
elif arv==0:
    print("Ei")
else:
    print("Arv on paaritu, nagu mina.")



#7.+ Eurokalkulaator - koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK vÃµi EEK->EUR.
#	kuvatakse korrektne arusaadav kÃ¼simus ja vastus - 1p
#	kuvatakse veateade, kui kasutaja tegi valiku valesti - 1p
#	kÃ¼sitakse valuuta kogust ja tehakse arvutused - 2p
#	kood kommenteeritud - 1p

#Ei oska

#8. TÃ¤ringud
#	kuvatakse korrektne arusaadav kÃ¼simus ja hiljem vastus - 1p
#	kasutaja vÃµistleb kahe tÃ¤ringuga arvuti vastu - 1p
#	kasutaja teeb pakkumise ning suurima tÃ¤ringupunktisumma vÃµitja saab laual oleva raha endale - 2p
#	kood kommenteeritud - 1p
	
#9. Emaili kontroll
#	kasutaja lisab emaili kujul enimi.pnimi@server.com - 1p
#	programm kontrollib kas email on sisestatud Ãµigesti - vÃ¤hemalt @-mÃ¤rgi kontroll - 1p
#	programm tÃ¼keldab selle ja vÃ¤ljastab lause: â€˜Tere enimi, sinu email on server serveris ja domeeniks on sul comâ€™ - 1p
#	kasutajalt kÃ¼situd kÃ¼simused on selgelt Ã¼heselt mÃµistetavad - 1p
#	kood kommenteeritud - 1p
	
#10. KaugushÃ¼pe
#	kasutaja sisestab 3 kaugushÃ¼ppe tulemust - 1p
#	sinu programm leiab ning vÃ¤ljastab parima ja keskmise tulemuse - 2p
#	programmi dialoog kasutajaga on arusaadav ja Ã¼heselt mÃµistetav - 1p
#	kood kommenteeritud - 1p
	
#11. Salakeel
#	sinu programm kÃ¼sib kasutajalt, kas ta soovib salakeelt luua vÃµi tÃµlkida - 1p
#	kasutaja sisestab tavalise sÃµna, mis muudetakse salakeeleks - 1p
#	kasutaja sisestab salakeeles sÃµna, mis teisendatakse jÃ¤lle normaalseks - 1p
#	kood kommenteeritud - 1p
	
#12. Eurokalkulaator
#	Koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK vÃµi EEK->EUR.
#	Oluline on kasutada kahte funktsiooni!!
	
#13. Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris vÃµi paaritu
#	kuvatakse korrektne arusaadav kÃ¼simus ja  vastus - 1p
#	eelnev kontroll, kas kasutaja ei lisanud arvu vÃµi pani nulli - 2p
#	kood mis teavitab paaris vÃµi paaritust arvust - 2p
#	kuvatakse programmi pealkiri - 1p

#14. Palkade vÃµrdlus - Loo palk.txt fail tÃ¶Ã¶tajate nime, soo ja palganumbriga (10 tÃ¶Ã¶tajat).
#	Koosta programm, mis analÃ¼Ã¼sib kas firmas toimub diskrimineerimist soo jÃ¤rgi. Selleks vÃµrdle omavahel meeste ja naiste palkade keskmiseid, samuti meeste ja naiste kÃµige kÃµrgemat palka. Programm peab tegema otsuse.

#	Hubert Hunt m 2340
#	Siim Siil m 2570
#	MÃ¤rt MÃ¤ger m 1960
#	Vilma Vihmauss n 2060
#	Merike Metskits n 2250
#	Kati Karu n 2370
#	Elmar Elevant m 2900
#	Timoteus Tigu m 2850
#	Reet Rebane n 2340
#	Kalev Kaamel m 2570
#	Karmen Kass n 2120
#	Kornelius Koer m 2250

#15.+ Temperatuurid - Programm peab tÃ¶Ã¶tlema Ã¼he aasta kÃµigi pÃ¤evade temperatuure. Kirjutada programm, mis leiab kuude kaupa, mitmendal kuupÃ¤eval oli kÃµige soojem. VÃ¤ljasta kuupÃ¤ev ja vastav temperatuur. (Kui sama temperatuuriga oli mitu pÃ¤eva, vÃ¤ljasta vÃ¤hemalt Ã¼ks)

#	jaanuar -16 -12 -15 -20 0 -1 -20 -2 -20 -14 -18 -8 2 -1 -14 -7 -15 -17 -6 -17 -17 -7 0 3 -20 -17 -15 -8 -12 3
#	veebruar -9 -2 -7 1 -16 -19 -19 -11 -16 -15 -9 -2 -16 -4 -20 -5 -6 -17 -5 0 -16 2 0 -20 -16 -2 -18
#	mÃ¤rts 2 -9 -1 -3 -6 -2 1 -2 -3 -9 -1 -4 0 -6 -7 1 0 2 -5 -10 2 -7 -3 2 -10 2 -9 -8 -5 -2
#	aprill -5 0 10 -9 0 -9 -8 6 -5 3 -1 4 9 -1 2 0 10 0 5 0 -10 0 6 3 -6 -2 -10 -8 -2
#	mai 12 5 8 -1 -2 4 10 -1 7 15 7 3 6 4 10 9 13 6 14 10 14 2 6 12 15 2 14 11 9 1
#	juuni 12 5 17 6 10 14 9 7 15 23 29 11 16 18 9 25 14 8 16 22 19 22 23 18 16 16 26 24 22
#	juuli 15 8 21 28 18 13 9 9 8 6 8 12 12 29 28 20 6 9 12 8 14 18 14 13 23 6 24 24 17 20
#	august 7 6 5 19 18 18 17 20 15 11 7 10 13 12 20 11 10 14 18 14 24 6 17 16 6 17 5 13 11
#	september 21 19 21 9 13 18 6 6 20 7 25 13 8 9 14 16 19 10 7 25 7 17 16 15 17 18 15 9 19
#	oktoober 2 2 1 5 -2 5 5 2 2 2 1 -2 1 -2 0 -2 5 4 0 1 -1 2 0 2 2 2 -1 1 4 -1
#	november -6 -7 -2 -7 -2 -4 0 -7 -8 -6 0 -9 -2 -3 -2 0 -8 -2 -5 -2 -5 -8 -10 0 -2 -9 -9 -7 -1
#	detsember -15 2 -11 -14 -15 -5 -5 -18 -18 -19 0 0 2 -7 -16 -7 -4 -1 -1 -16 -18 -10 -3 -19 -6 -16 -16 -8 -2 -18

#Ei oska
	
#16.+ TÃ¤ringud
#	Kasutaja vÃµistleb kahe tÃ¤ringuga arvuti vastu. Kasutaja teeb pakkumise ning suurima tÃ¤ringupunktisumma vÃµitja saab laual oleva raha endale juurde. MÃ¤ng kestab kuni kummalgi on raha otsas.
#	(Vihjed: kÃ¼si kasutajalt nime, kuva pidevalt konto seisu ja tÃ¤ringuviskeid, kasutajate raha hulga mÃ¤ngu alguses mÃ¤Ã¤rad sina)

#Ei oska

#17. Email
#	Kasutaja lisab emaili kujul enimi.pnimi@server.com
#	Programm kontrollib kas email on sisestatud Ãµigesti
#	Programm tÃ¼keldab selle ja vÃ¤ljastab lause: Tere enimi, sinu email on server serveris ja domeeniks on sul com
	
