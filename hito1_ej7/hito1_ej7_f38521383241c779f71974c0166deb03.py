#Zodiaco
D = int(input("Ingrese dia de cumpleaños:"))
M = int(input("Ingrese mes de cumpleaños:"))

if ((M == 3) and (D >= 21)) or ((M == 4) and (D <= 20)):
    print("Aries")
if ((M == 4) and (D >= 20)) or ((M == 5) and (D <= 21)):
    print("Tauro")
if ((M == 5) and (D >= 21)) or ((M == 6) and (D <= 21)):
    print("Geminis")
if ((M == 6) and (D >= 21)) or ((M == 7) and (D <= 23)):
    print("Cancer")
if ((M == 7) and (D >= 23)) or ((M == 8) and (D <= 23)):
    print("Leo")
if ((M == 8) and (D >= 23)) or ((M == 9) and (D <= 23)):
    print("Virgo")
if ((M == 9) and (D >= 23)) or ((M == 10) and (D <= 23)):
    print("Libra")
if ((M == 10) and (D >= 23)) or ((M == 11) and (D <= 22)):
    print("Escorpio")
if ((M == 11) and (D >= 23)) or ((M == 12) and (D <= 22)):
    print("Sagitario")
if ((M == 12) and (D >= 22)) or ((M == 1) and (D <= 20)):
    print("Capricornio")
if ((M == 1) and (D >= 20)) or ((M == 2) and (D <= 19)):
    print("Acuario")
if ((M == 2) and (D >= 19)) or ((M == 3) and (D <= 21)):
    print("Piscis")