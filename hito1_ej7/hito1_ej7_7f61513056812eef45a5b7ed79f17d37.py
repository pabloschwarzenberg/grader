#Zodiaco
x=int(input("Ingrese dia de nacimiento: "))
y=int(input("Ingrese mes de nacimiento: "))
if (22<x<=31 and 3 == y) or (1 <= x <= 20 and 4 == y):
    print("Aries")
if (21<=x<=30 and 4 == y) or (1 <= x <= 21 and 5 == y):
    print("Tauro")
if (22<=x<=31 and 5 == y)  or (1 <= x <= 21 and 6 == y):
    print("Geminis")
if (22<=x<=30 and 6 == y)  or (1 <= x <= 22 and 7 == y):
    print("Cancer")
if (23<=x<=31 and 7 == y)  or (1 <= x <= 22 and 8 == y):
    print("Leo")
if (23<=x<=31 and 8 == y)  or (1 <= x <= 23 and 9 == y):
    print("Virgo")
if (24<=x<=30 and 9 == y)  or (1 <= x <= 23 and 10 == y):
    print("Libra")
if (24<=x<=31 and 10 == y)  or (1 <= x <= 22 and 11 == y):
    print("Escorpio")
if (23<x<=30 and 11 == y)  or (1 <= x <= 21 and 12 == y):
    print("Sagitario")
if (22<x<=31 and 12 == y) or (1 <= x <= 20 and 1 == y):
    print("Capricornio")
if (21 < x <= 31 and 1 == y) or (1 <= x <= 19 and 2 == y):
    print("Acuario")
if (20 < x <= 28 and 2 == y) or (1 <= x <= 20 and 3 == y):
    print("Piscis")