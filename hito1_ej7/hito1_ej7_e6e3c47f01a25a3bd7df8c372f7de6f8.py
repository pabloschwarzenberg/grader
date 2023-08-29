#Zodiaco
print("Determinar signo del Zodíaco\n\n")

dia=int(input("Ingrese el día de cumpleaños: "))
mes=int(input("Ingrese el mes de cumpleaños: "))

if(dia >=21 and mes==3) or (dia <= 20 and mes==4):
    print("Aries")
elif (dia >=21 and mes==4) or (dia <= 21 and mes==5):
    print("Tauro")
elif (dia >=22 and mes==5) or (dia <= 21 and mes==6):
    print("Geminis")
elif (dia >=26 and mes==6) or (dia <= 23 and mes==7):
    print("Cancer")
elif (dia >=24 and mes==7) or (dia <= 23 and mes==8):
    print("Leo")
elif (dia >=24 and mes==8) or (dia <= 23 and mes==9):
    print("Virgo")
elif (dia >=24 and mes==9) or (dia <= 23 and mes==10):
    print("Libra")
elif (dia >=24 and mes==10) or (dia <= 22 and mes==11):
    print("Escorpión")
elif (dia >=23 and mes==11) or (dia <= 22 and mes==12):
    print("Sagitario")
elif (dia >=23 and mes==12) or (dia <= 20 and mes==1):
    print("Capricornio")
elif (dia >=21 and mes==1) or (dia <= 19 and mes==2):
    print("Acuario")
elif (dia >=20 and mes==3) or (dia < 21 and mes==3):
    print("Piscis")
     