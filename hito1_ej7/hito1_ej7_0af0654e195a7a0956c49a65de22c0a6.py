#Zodiaco
dia = int(input("Ingrese el dia de su cumpleaños"))
mes = int(input("Ingrese el mes de su cumpleaños"))

if mes == 1 and dia >= 20 and dia <= 31:
    print("ACUARIO")
else:
    if mes == 2 and dia <= 19:
        print("ACUARIO")

if mes == 2 and dia >= 20 and dia <= 28:
    print("PISCIS")
else:
    if mes == 3 and dia < 21:
        print("PISCIS")
if mes == 3 and dia >= 21 and dia <= 31:
    print("ARIES")
else:
    if mes == 4 and dia < 21:
        print("ARIES")
if mes == 4 and dia >= 21 and dia <= 30:
    print("TAURO")
else:
    if mes == 5 and dia < 22:
        print("TAURO")
if mes == 5 and dia >= 22 and dia <= 31:
    print("GEMINIS")
else:
    if mes == 6 and dia < 22:
        print("GEMINIS")
if mes == 6 and dia >= 22 and dia <= 30:
    print("CANCER")
else:
    if mes == 7 and dia < 23:
        print("CANCER")
if mes == 7 and dia >= 23 and dia <= 31:
    print("LEO")
else:
    if mes == 8 and dia < 23:
        print("LEO")
if mes == 8 and dia >= 23 and dia <= 31:
    print("VIRGO")
else:
    if mes == 9 and dia < 24:
        print("VIRGO")
if mes == 9 and dia >= 24 and dia <= 30:
    print("LIBRA")
else:
    if mes == 10 and dia < 24:
        print("LIBRA")
if mes == 10 and dia >= 24 and dia <= 31:
    print("ESCORPION")
else:
    if mes == 11 and dia < 23:
        print("ESCORPION")
if mes == 11 and dia >= 23 and dia <= 30:
    print("SAGITARIO")
else:
    if mes == 12 and dia < 22:
        print("SAGITARIO")
if mes == 12 and dia >= 22 and dia <= 31:
    print("CAPRICORNIO")
else:
    if mes == 1 and dia < 20:
        print("CAPRICORNIO")