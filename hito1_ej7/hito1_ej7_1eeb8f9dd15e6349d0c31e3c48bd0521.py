#Zodiaco
dia=int(input("Ingrese día de su nacimiento: "))
mes=int(input("ingrese mes su nacimiento: "))
if (dia>=21 and dia<=31 and mes==3) or (dia>=1 and dia<20 and mes==4) :
    print("su signo es Aries")
if (dia>=20 and dia<=31 and mes==4) or (dia>=1 and dia<21 and mes==5) :
    print("su signo es Tauro")
if (dia >= 21 and dia <= 31 and mes == 5) or (dia >= 1 and dia < 23 and mes == 6):
    print("su signo es Géminis")
if (dia>=21 and dia<=31 and mes==6) or (dia>=1 and dia<23 and mes==7) :
    print("su signo es Cáncer")
if (dia>=23 and dia<=31 and mes==7) or (dia>=1 and dia<23 and mes==8) :
    print("su signo es Leo")
if (dia>=23 and dia<=31 and mes==8) or (dia>=1 and dia<23 and mes==9) :
    print("su signo es Virgo")
if (dia>=23 and dia<=31 and mes==9) or (dia>=1 and dia<23 and mes==10) :
    print("su signo es Libra")
if (dia >= 23 and dia <= 31 and mes == 10) or (dia >= 1 and dia < 22 and mes == 11):
    print("su signo es Ecorpio")
if (dia >= 22 and dia <= 31 and mes == 11) or (dia >= 1 and dia < 22 and mes == 12):
    print("su signo es Sagitario")
if (dia >= 22 and dia <= 31 and mes == 12) or (dia >= 1 and dia < 20 and mes == 1):
    print("su signo es capricornio")
if (dia >= 20 and dia <= 31 and mes == 1) or (dia >= 1 and dia < 19 and mes == 2):
    print("su signo es acuario")
if (dia >= 19 and dia <= 31 and mes == 2) or (dia >= 1 and dia < 21 and mes == 3):
    print("su signo es piscis")

