#Zodiaco
#Calcular tu signo del horoscopo, segun tu dia y mes de nacimiento:
dia = int(input("Ingresa el dia en el que naciste: "))
mes = int(input("Ingresa el mes en el que naciste: "))

if (dia > 31) or (mes > 12):
    print ("Esa fecha no existe")
          
elif (dia > 21 and mes == 3) or (dia < 19 and mes == 4):
    print("aries")

elif (dia > 20 and mes == 4) or (dia < 20 and mes == 5):
    print("tauro")

elif (dia > 21 and mes == 5) or (dia < 20 and mes == 6):
    print("géminis")
    
elif (dia > 21 and mes == 6) or (dia < 22 and mes == 7):
    print("cáncer")

elif (dia > 23 and mes == 7) or (dia < 22 and mes == 8):
    print("leo")

elif (dia > 23 and mes == 8) or (dia < 22 and mes == 9):
    print("virgo")

elif (dia > 23 and mes == 9) or (dia < 22 and mes == 10):
    print("libra")

elif (dia > 23 and mes == 10) or (dia < 21 and mes == 11):
    print("escorpión")

elif (dia > 22 and mes == 11) or (dia < 21 and mes == 12):
    print("sagitario")

elif (dia > 22 and mes == 12) or (dia < 19 and mes == 1):
    print("capricornio")

elif (dia > 20 and mes == 1) or (dia < 18 and mes == 2):
    print("acuario")

elif (dia > 19 and mes == 2) or (dia < 20 and mes == 3):
    print("piscis")
     