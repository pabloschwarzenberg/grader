#Zodiaco
dia = int(input('Ingresa el día de tu cumpleaños: '))
mes = int(input('Ingresa el mes de tu cumpleaños: '))

if (dia >= 21 and mes == 3) or (dia < 20 and mes == 4):
    print('ARIES') 
if (dia >= 20 and mes == 4) or (dia < 21 and mes == 5):
   print("TAURO")
if (dia >= 21 and mes == 5) or (dia < 21 and mes == 6):
    print("GEMINIS")
if (dia >= 21 and mes == 6) or (dia < 23 and mes == 7):
    print("CANCER")
if (dia >= 23 and mes == 7) or (dia < 23 and mes == 8):
    print("LEO")
if (dia >= 23 and mes == 8) or (dia < 23 and mes == 9):
    print("VIRGO")
if (dia >= 23 and mes == 9) or (dia < 23 and mes == 10):
    print("LIBRA")
if (dia >= 23 and mes == 10) or (dia < 23 and mes == 11):
    print("ESCORPIO")
if (dia >= 22 and mes == 11) or (dia < 22 and mes == 12):
    print("SAGITARIO")
if (dia >= 22 and mes == 12) or (dia < 20 and mes == 1):
    print("CAPRICORNIO")
if (dia >= 20 and mes == 1) or (dia < 19 and mes == 2):
    print("ACUARIO")
if (dia >= 19 and mes == 2) or (dia < 21 and mes == 3):
    print("PISCIS")
