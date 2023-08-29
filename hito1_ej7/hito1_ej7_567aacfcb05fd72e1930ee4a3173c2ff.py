#Zodiaco

Dia = int(input("Ingrese su día de nacimiento: "))
Mes = int(input("Ingrese su mes de nacimiento: "))

while (Dia < 1 or Dia > 31):
    print("Un mes no tiene días inferiores a 1 o superiores a 31")
    Dia = int(input("Ingrese su día de nacimiento: "))

while (Mes < 1 or Mes > 12):
    print("Un año no tiene meses inferiores a 1 o superiores a 12")
    Mes = int(input("Ingrese su mes de nacimiento: "))

if ((Mes == 3 and 21 <= Dia <= 31) or (Mes == 4 and 1 <= Dia < 20)):
    print("Aries")

elif ((Mes == 4 and 20 <= Dia <= 30) or (Mes == 5 and 1 <= Dia < 21)):
    print("Tauro")

elif ((Mes == 5 and 21 <= Dia <= 31) or (Mes == 6 and 1 <= Dia < 21)):
    print("Gemini")

elif ((Mes == 6 and 21 <= Dia <= 30) or (Mes == 7 and 1 <= Dia < 23)):
    print("Cancer")

elif ((Mes == 7 and 23 <= Dia <= 31) or (Mes == 8 and 1 <= Dia < 23)):
    print("Leo")

elif ((Mes == 8 and 23 <= Dia <= 30) or (Mes == 9 and 1 <= Dia < 23)):
    print("Virgo")

elif ((Mes == 9 and 23 <= Dia <= 30) or (Mes == 10 and 1 <= Dia < 23)):
    print("Libra")

elif ((Mes == 10 and 23 <= Dia <= 31) or (Mes == 11 and 1 <= Dia <= 22)):
    print("Escorpio")

elif ((Mes == 11 and 23 <= Dia <= 30) or (Mes == 12 and 1 <= Dia < 22)):
    print("Sagitario")

elif ((Mes == 12 and 22 <= Dia <= 31) or (Mes == 1 and 1 <= Dia < 20)):
    print("Capricornio")

elif ((Mes == 1 and 23 <= Dia <= 31) or (Mes == 2 and 1 <= Dia < 19)):
    print("Acuario")

elif ((Mes == 2 and 19 <= Dia <= 28) or (Mes == 3 and 1 <= Dia < 21)):
    print("Piscies")