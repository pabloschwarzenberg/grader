#Zodiaco
dia = int(input("Ingrese Dia de Nacimiento"))
mes = int(input("Ingrese Mes de Nacimiento"))

#1,2,3,4,5,6,7,8,9,10,11,12

if dia >= 20 and mes == 1 or dia <= 18 and mes == 2:
    print("Acuario")
elif dia >= 19 and mes == 2 or dia <= 20 and mes == 3:
    print("Piscis")
elif dia >= 21 and mes == 3 or dia <= 20 and mes == 4:
    print("Aries")
elif dia >= 21 and mes == 4 or dia <= 21 and mes == 5:
    print("Tauro")
elif dia >= 22 and mes == 5 or dia <= 21 and mes == 6:
    print("Geminis")
elif dia >= 22 and mes == 6 or dia <= 22 and mes == 7:
    print("Cancer")
elif dia >= 23 and mes == 7 or dia <= 23 and mes == 8:
    print("Leo")
elif dia >= 24 and mes == 8 or dia <= 23 and mes == 9:
    print("Virgo")
elif dia >= 24 and mes == 9 or dia <= 23 and mes == 10:
    print("Libra")
elif dia >= 24 and mes == 9 or dia <= 22 and mes == 11:
    print("Escorpion")
elif dia >= 23 and mes == 11 or dia <= 21 and mes == 12:
    print("Sagitario")
elif dia >= 22 and mes == 12 or dia <= 20 and mes == 1:
    print("Capricornio")
else:
    print("Signo no encontrado")