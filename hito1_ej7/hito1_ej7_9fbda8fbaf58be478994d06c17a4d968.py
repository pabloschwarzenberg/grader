#Zodiaco
D = int(input("Indique su dia de nacimiento: "))
M = int(input("Indique su mes de nacimiento: "))

if D >= 21 and M == 3 or D <= 20 and M == 4:
    print("Aries")

elif D >= 21 and M == 4 or D <= 20 and M == 5:
    print("Tauro")

elif D >= 21 and M == 5 or D <= 21 and M == 6:
    print("Geminis")

elif D >= 22 and M == 6 or D <= 22 and M == 7:
    print("Cancer")

elif D >= 23 and M == 7 or D <= 22 and M == 8:
    print("Leo")

elif D >= 23 and M == 8 or D <= 22 and M == 9:
    print("Virgo")

elif D >= 23 and M == 9 or D <= 22 and M == 10:
    print("Libra")

elif D >= 23 and M == 10 or D <= 22 and M == 11:
    print("Escorpio")

elif D >= 23 and M == 11 or D <= 21 and M == 12:
    print("Sagitario")

elif D >= 22 and M == 12 or D <= 20 and M == 1:
    print("Capricornio")

elif D >= 21 and M == 1 or D <= 18 and M == 2:
    print("Acuario")

elif D >= 19 and M == 2 or D <= 20 and M == 3:
    print("Piscis")

else:
    print("fin del programa")