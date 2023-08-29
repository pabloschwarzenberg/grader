#Zodiaco
día = int(input("Ingrese el número de día de nacimiento: ")) 
mes = int(input("Ingrese el día del mes de nacimiento: "))

if (día >= 21 and mes == 3) or (día <= 20 and mes == 4):
    print("aries")
elif (día >= 20 and mes == 4) or (día <= 21 and mes == 5):
    print("tauro")
elif (día >= 21 and mes == 5) or (día <= 21 and mes == 6):
    print("géminis")
elif (día >= 21 and mes == 6) or (día <= 23 and mes == 7):
    print("cáncer")
elif (día >= 23 and mes == 7) or (día <= 23 and mes == 8):
    print("leo")
elif (día >= 23 and mes == 8) or (día <= 23 and mes == 9):
    print("virgo")
elif (día >= 23 and mes == 9) or (día <= 23 and mes == 10):
    print("libra")
elif (día >= 23 and mes == 10) or (día <= 22 and mes == 11):
    print("escorpio")
elif (día >= 22 and mes == 11) or (día <= 22 and mes == 12):
    print("sagitario")
elif (día >= 22 and mes == 12) or (día <= 20 and mes == 1):
    print("capricornio")
elif (día >= 20 and mes == 1) or (día <= 19 and mes == 2):
    print("acuario")
else:
    print("piscis")