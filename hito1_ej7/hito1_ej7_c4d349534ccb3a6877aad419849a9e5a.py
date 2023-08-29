#Zodiaco
x = int(input("Día: "))
y = int(input("Mes: "))

if (y == 3 and x >= 21) or (y == 4 and x <= 19):
    print("ARIES")

if (y == 4 and x >= 20) or (y == 5 and x <= 20):
    print("TAURO")

if (y == 5 and x >= 20) or (y == 6 and x <= 20):
    print("GEMINIS")

if (y == 6 and x >= 22) or (y == 7 and x <= 22):
    print("CANCER")

if (y == 7 and x >= 22) or (y == 8 and x <= 22):
    print("LEO")

if (y == 8 and x >= 23) or (y == 9 and x <= 22):
    print("VIRGO")

if (y == 9 and x >= 23) or (y == 10 and x <= 22):
    print("LIBRA")

if (y == 10 and x >= 23) or (y == 11 and x <= 21):
    print("ESCORPIO")

if (y == 11 and x >= 22) or (y == 12 and x <= 21):
    print("SAGITARIO")

if (y == 12 and x >= 22) or (y == 1 and x <= 19):
    print("CAPRICORNIO")

if (y == 1 and x >= 20) or (y == 2 and x <= 18):
    print("ACUARIO")

if (y == 2 and x >= 19) or (y == 3 and x <= 20):
    print("PISCIS")