#Zodiaco
Dia = int(input("Ingrese su dia de nacimiento: "))
Mes = int(input("ingrese su mes de nacimiento: "))
if (Mes == 3 and Dia >= 21)or(Mes == 4 and Dia <= 20):
    print("Aries")
elif (Mes == 4 and Dia >= 20)or(Mes == 5 and Dia <= 21):
    print("Tauro")
elif (Mes == 5 and Dia >= 21)or(Mes == 6 and Dia <= 21):
    print("Geminis")
elif(Mes == 6 and Dia >= 21)or(Mes == 7 and Dia <= 23):
    print("Cancer")
elif (Mes == 7 and Dia >= 23)or(Mes == 8 and Dia <= 23):
    print("Leon")
elif (Mes == 8 and Dia >= 23)or(Mes == 9 and Dia <= 23):
    print("Virgo")
elif (Mes == 9 and Dia >= 23)or(Mes == 10 and Dia <= 23):
    print("Libra")
elif (Mes == 10 and Dia >= 23)or(Mes == 11 and Dia <= 22):
    print("Escorpion")
elif (Mes == 11 and Dia >= 23)or(Mes == 12 and Dia <= 23):
    print("Sagitario")
elif (Mes == 12 and Dia >= 22)or(Mes == 1 and Dia <= 20):
    print("Capricornio")
elif (Mes == 1 and Dia >= 20)or(Mes == 2 and Dia <= 19):
    print("Acuario")
#elif (Mes == 2 and Dia >= 19)or(Mes == 3 and Dia <= 21):
 #   print("Piscis")
else:
    print("Piscis")