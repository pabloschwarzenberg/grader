print("Calculador del signo del zodiaco (Tropical)")

a = int(input("Ingrese su dia de cumpleaños:"))
while a >= 32 or a < 1:
    a = int(input("Ingrese su dia de cumpleaños:"))
b = int(input("Ingrese su mes de cumpleaños:"))
while b > 12 or b < 1:
    b = int(input("Ingrese su mes de cumpleaños:"))

while (b == 4 or b == 6 or b == 8 or b == 10 or b == 12) and a > 30:
    a = int(input("Ingrese su dia de cumpleaños:"))
    b = int(input("Ingrese su mes de cumpleaños:"))
while b == 2 and a > 28:
    a = int(input("Ingrese su dia de cumpleaños:"))
if (a >= 21 and b == 3) or (a <= 20 and b == 4):
    print("Usted es Aries")
if (a >= 21 and b == 4) or (a <=20 and b == 5):
    print("Usted es Tauro")
if (a >= 21 and b == 5) or (a <= 21 and b == 6):
    print("Usted es Géminis")
if (a >= 22 and b == 6) or (a <= 22 and b == 7):
    print("Usted es Cáncer")
if (a >= 23 and b == 7) or (a <= 23 and b == 8):
    print("Usted es Leo")
if (a >= 24 and b == 8) or (a <= 22 and b == 9):
    print("Usted es Virgo")
if (a >= 23 and b == 9) or (a <= 22 and b == 10):
    print("Usted es Libra")
if (a >= 23 and b == 10) or (a <= 22 and b == 11):
    print("Usted es Escorpio")
if (a >= 23 and b == 11) or (a <= 21 and b == 12):
    print("Usted es Sagitario")
if (a >= 22 and b == 12) or (a <= 20 and b == 1):
    print("Usted es Capricornio")
if (a >= 21 and b == 1) or (a <= 19 and b == 2):
    print("Usted es Acuario")
if (a >= 20 and b == 2) or (a <= 20 and b == 3):
    print("Usted es Piscis")