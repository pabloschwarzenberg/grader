#Zodiaco
d = eval(input("Día: "))
m = eval(input("Mes: "))

if 31 >= d >= 21 and m == 3 or d <=20 and m == 4:
    print("Aries")
if 30 >= d >= 20 and m == 4 or d <=21 and m == 5:
    print("Tauro")
if 31 >= d >= 21 and m == 5 or d <=21 and m == 6:
    print("Geminis")
if 30 >= d >= 21 and m == 6 or d <=23 and m == 7:
    print("cancer")
if 31 >= d >= 23 and m == 7 or d <=23 and m == 8:
    print("Leo")
if 31 >= d >= 23 and m == 8 or d <=23 and m == 9:
    print("Virgo")
if 30 >= d >= 21 and m == 9 or d <=20 and m == 10:
    print("Libra")
if 31 >= d >= 23 and m == 10 or d <=22 and m == 11:
    print("Escorpión")
if 30 >= d >= 22 and m == 12 or d <=22 and m == 1:
    print("Sagitario")
if 31 >= d >= 22 and m == 1 or d <=20 and m == 2:
    print("Capricornio")
if 31 >= d >= 20 and m == 3 or d <=19 and m == 4:
    print("Acuario")
if 28 >= d >= 19 and m == 3 or d <=21 and m == 4:
    print("piscis")