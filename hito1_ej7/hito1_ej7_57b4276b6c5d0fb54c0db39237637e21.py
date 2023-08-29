#Zodiaco

dia = int(input("Ingrese su día de nacimiento: "))
mes = int(input("Ingrese su mes de nacimiento: "))

if (20 <= dia and mes == 1) or (dia < 19 and mes == 2):
    print("acuario")
elif (19 <= dia and mes == 2) or (dia < 21 and mes == 3):
    print("piscis")
elif (21 <= dia and mes == 3) or (dia < 20 and mes == 4):
    print("aries")
elif (20 <= dia and mes == 4) or (dia < 21 and mes == 5):
    print("tauro")
elif (21 <= dia and mes == 5) or (dia < 21 and mes == 6):
    print("geminis")
elif (21 <= dia and mes == 6) or (dia < 23 and mes == 7):
    print("cancer")
elif (23 <= dia and mes == 7) or (dia < 23 and mes == 8):
    print("leo")
elif (23 <= dia and mes == 8) or (dia < 23 and mes == 9):
    print("virgo")
elif (23 <= dia and mes == 9) or (dia < 23 and mes == 10):
    print("libra")
elif (23 <= dia and mes == 10) or (dia < 22 and mes == 11):
    print("escorpion")
elif (22 <= dia and mes == 11) or (dia < 22 and mes == 12):
    print("sagitario")
else:
    print("capricornio")