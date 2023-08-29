#Zodiaco
dia = int(input("Ingrese el dia de nacimiento: "))
mes = int(input("Ingrese el mes de nacimiento: "))

if (dia >= 20 and mes == 1) or (dia <= 18 and mes == 2):
    print("Perteneces al signo de Acuario")
    
elif (dia >= 19 and mes == 2) or (dia <= 20 and mes == 3):
    print("Perteneces al signo de Piscis")
    
elif (dia >= 21 and mes == 3) or (dia <= 19 and mes == 4):
    print("Perteneces al signo de Aries")
elif (dia >= 20 and mes == 4) or (dia <= 20 and mes == 5):
    print("Perteneces al signo de Tauro")
elif (dia >= 21 and mes == 5) or (dia <= 20 and mes == 6):
    print("Perteneces al signo de Geminis")
elif (dia >= 21 and mes == 6) or (dia <= 22 and mes == 7):
    print("Perteneces al signo de Cancer")
elif (dia >= 23 and mes == 7) or (dia <= 22 and mes == 8):
    print("Perteneces al signo de Leo")
elif (dia >= 23 and mes == 8) or (dia <= 22 and mes == 9):
    print("Perteneces al signo de Virgo")
elif (dia >= 23 and mes == 9) or (dia <= 22 and mes == 10):
    print("Perteneces al signo de Libra")
elif (dia >= 23 and mes == 10) or (dia <= 21 and mes == 11):
    print("Perteneces al signo de Escorpio")
elif (dia >= 22 and mes == 11) or (dia <= 21 and mes == 12):
    print("Perteneces al signo de Sagitario")
elif (dia >= 22 and mes == 12) or (dia <= 19 and mes == 1):
    print("Perteneces al signo de Capricornio")
else:
    print("Fecha no valida")
          