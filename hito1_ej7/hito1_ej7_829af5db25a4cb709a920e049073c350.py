#zodiaco

dia = int(input("Ingrese el dia: "))
mes = int(input("Ingrese su mes: "))



if (dia >= 21 and mes == 3) or (dia <=20 and mes == 4) :
    signo = ("aries")
if (dia >= 21 and mes == 4) or (dia <=21 and mes == 5):
    signo = ("tauro")
if (dia >= 2 and mes == 5) or (dia <=21 and mes == 6):
    signo = ("geminis")
if (dia >= 21 and mes == 6) or (dia <=23 and mes ==7):
    signo = ("cancer")
if (dia >= 23 and mes == 7) or (dia <=23 and mes == 8):
    signo = ("leo")
if (dia >= 23 and mes == 8) or (dia <=23 and mes == 9):
    signo = ("virgo")
if (dia >= 23 and mes == 9) or (dia <=22 and mes == 10):
    signo = ("libra")
if (dia >= 23 and mes == 10) or (dia <=22 and mes == 11):
    signo = ("escorpio")
if (dia >= 23 and mes == 11) or (dia <=22 and mes == 12):
    signo = ("sagitario")
if (dia >= 22 and mes == 12) or (dia <=20 and mes == 1):
    signo = ("capricornio")
if (dia >= 20 and mes == 1) or (dia <=19 and mes == 2):
    signo = ("acuario")
if (dia >= 19 and mes == 2) or (dia <=21 and mes == 3):
    signo = ("piscis")

print("Su signo es ", signo)