#Zodiaco
#INICIO

A = int(input("Ingrese su día de cumpleaños: "))
while A >= 32 or A < 1:
    A = int(input("Ingrese su día de cumpleaños: "))
B = int(input("Ingrese su mes de cumpleaños: "))
while B > 12 or B < 1:
    B = int(input("Ingrese su mes de cumpleaños: "))
    
#LIMITACIÓN DE NÚMEROS
    
while (B == 4 or B == 6 or B == 8 or B == 10 or B == 12) and A > 30:
    A = int(input("Ingrese su día de cumpleaños: "))
    B = int(input("Ingrese su mes de cumpleaños: "))
while A > 28 and B == 2:
    A = int(input("Ingrese su día de cumpleaños: "))
    
#SIGNOS
if (A >= 21 and B == 3) or (A <= 20 and B == 4):
    print("Tu signo es: Aries")
if (A >= 21 and B == 4) or (A <=20 and B == 5):
    print("Tu signo es: Tauro")
if (A >= 21 and B == 5) or (A <= 21 and B == 6):
    print("Tu signo es: Géminis")
if (A >= 22 and B == 6) or (A <= 22 and B == 7):
    print("Tu signo es: Cáncer")
if (A >= 23 and B == 7) or (A <= 23 and B == 8):
    print("Tu signo es: Leo")
if (A >= 24 and B == 8) or (A <= 22 and B == 9):
    print("Tu signo es: Virgo")
if (A >= 23 and B == 9) or (A <= 22 and B == 10):
    print("Tu signo es: Libra")
if (A >= 23 and B == 10) or (A <= 22 and B == 11):
    print("Tu signo es: Escorpio")
if (A >= 23 and B == 11) or (A <= 21 and B == 12):
    print("Tu signo es: Sagitario")
if (A >= 22 and B == 12) or (A <= 20 and B == 1):
    print("Tu signo es: Capricornio")
if (A >= 21 and B == 1) or (A <= 19 and B == 2):
    print("Tu signo es: Acuario")
if (A >= 20 and B == 2) or (A <= 20 and B == 3):
    print("Tu signo es: Piscis")

