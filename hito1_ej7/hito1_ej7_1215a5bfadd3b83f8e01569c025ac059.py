#Zodiaco
print("Su signo del zodíaco es necesario ->")
dia = int(input("Día de su cumpleaños ->"))
mes = int(input("Mes de su cumpleaños-> "))
if (dia >= 21 and mes == 3) or (dia <= 20 and mes == 4):
    signo =("aries")
elif (dia >= 21 and mes == 4) or (dia <=21 and mes == 5):
    signo = ("tauro")
elif (dia >= 2 and mes == 5) or (dia <=21 and mes == 6):
    signo = ("geminis")
elif (dia >= 21 and mes == 6) or (dia <=23 and mes ==7):
    signo = ("cáncer")
elif (dia >= 23 and mes == 7) or (dia <=23 and mes == 8):
    signo = ("leo")
elif (dia >= 23 and mes == 8) or (dia <=23 and mes == 9):
    signo = ("virgo")
elif (dia >= 23 and mes == 9) or (dia <=22 and mes == 10):
    signo = ("libra")
elif (dia >= 23 and mes == 10) or (dia <=22 and mes == 11):
    signo = ("escorpio")
elif (dia >= 23 and mes == 11) or (dia <=22 and mes == 12):
    signo = ("sagitario")
elif (dia >= 22 and mes == 12) or (dia <=20 and mes == 1):
    signo = ("capricornio")
elif (dia >= 20 and mes == 1) or (dia <=19 and mes == 2):
    signo = ("acuario")
elif (dia >= 19 and mes == 2) or (dia <=21 and mes == 3):
    signo = ("piscis")
print("El signo que le asigno su carta astral es...", signo )      