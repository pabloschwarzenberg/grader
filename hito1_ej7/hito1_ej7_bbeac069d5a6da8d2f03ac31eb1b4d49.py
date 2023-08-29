#Entrada
Dia = int(input("Dia de nacimiento: "))
Mes = int(input("Mes de nacimiento(en numeros de 1-12): "))

#Signo
if Mes == 1:
    if Dia < 20:
     print("Eres Capricornio")
    else:
        print("Eres Acuario")

elif Mes == 2:
    if Dia < 19:
     print("Eres Acuario")
    else:
        print("Eres Piscis")

elif Mes == 3:
    if Dia < 21:
     print("Eres Piscis")
    else:
        print("Eres Aries")

elif Mes == 4:
    if Dia < 20:
     print("Eres Aries")
    else:
        print("Eres Tauro")

elif Mes == 5:
    if Dia < 21:
     print("Eres Tauro")
    else:
        print("Eres Geminis")

elif Mes == 6:
    if Dia < 21:
     print("Eres Geminis")
    else:
        print("Eres Cancer")
elif Mes == 7:
    if Dia < 23:
     print("Eres Cancer")
    else:
        print("Eres Leo")
elif Mes == 8:
    if Dia < 23:
     print("Eres Leo")
    else:
        print("Eres Virgo")
elif Mes == 9:
    if Dia < 23:
     print("Eres Virgo")
    else:
        print("Eres Libra")
elif Mes == 10:
    if Dia < 23:
     print("Eres Libra")
    else:
        print("Eres Escorpion")
elif Mes == 11:
    if Dia < 22:
     print("Eres Escorpion")
    else:
        print("Eres Sagitario")
elif Mes == 12:
    if Dia < 22:
     print("Eres Sagitario")
    else:
        print("Eres Capricornio")