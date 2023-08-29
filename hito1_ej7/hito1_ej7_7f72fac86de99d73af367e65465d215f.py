#Zodiaco
#entradas
#entradas
dia = float(input("favor escriba el numero de dia de nacimiento: "))
mes = int(input("favor escriba el mes de su nacimiento: "))

if (dia >= 21 and mes == 3) or (dia <= 19 and mes == 4):
    print("es aries")
elif(dia >= 20 and mes == 4) or (dia <= 20 and mes == 5):
    print("es tauro")
elif (dia >= 21 and mes == 5) or (dia <= 20 and mes == 6):
    print("es geminis")
elif (dia >= 21 and mes == 6) or (dia <= 22 and mes == 7):
    print("es cancer")
elif (dia >= 23 and mes == 7) or (dia <= 22 and mes == 8):
    print("es leo")
elif (dia >= 23 and mes == 8) or (dia <= 22 and mes == 9):
    print("es virgo")
elif (dia >= 23 and mes == 9) or (dia <= 22 and mes == 10):
    print("es libra")
elif (dia >= 23 and mes == 10) or (dia <= 21 and mes == 11):
    print("es escorpion")
elif (dia >= 22 and mes == 11) or (dia <= 21 and mes == 12):
    print("es sagitario")
elif (dia >= 22 and mes == 12) or (dia <= 19 and mes == 1):
    print("es capricornio")
elif (dia >= 20 and mes == 1) or (dia <= 18 and mes == 2):
    print("acuario")
elif (dia >= 19 and mes == 2) or (dia <= 20 and mes == 3):
    print("piscis")
