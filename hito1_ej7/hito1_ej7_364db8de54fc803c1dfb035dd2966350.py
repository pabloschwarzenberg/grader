#Entrada de Datos
dia_de_nacimiento = int(input("Indique su dia de cumpleaños: "))
if dia_de_nacimiento <= 31 and dia_de_nacimiento >= 1:
    print("Resulta valido")
else:
    print("ingrese una opcion valida")

Mes_de_nacimiento = int(input("Indique el mes de su cumpleaños con numeros: "))
if Mes_de_nacimiento >= 1 and Mes_de_nacimiento <= 12:
    print("Resulta valido")
else:
    print("ingrese una opcion valida")

#calcular signo
if dia_de_nacimiento >= 21 and Mes_de_nacimiento == 3:
    print("Su signo zodiacal es Aries")
elif dia_de_nacimiento <= 20 and Mes_de_nacimiento == 4:
    print("Su signo zodiacal es Aries")
elif dia_de_nacimiento >= 20 and Mes_de_nacimiento == 4:
    print("Su Signo Zodiacal es Tauro")
elif dia_de_nacimiento <= 21 and Mes_de_nacimiento == 5:
    print("Su Signo Zodiacal es Tauro")
elif dia_de_nacimiento >= 21 and Mes_de_nacimiento == 5:
    print("Su Signo Zodiacal es Geminis")
elif dia_de_nacimiento <= 21 and Mes_de_nacimiento == 6:
    print("Su Signo Zodiacal es Geminis")
elif dia_de_nacimiento >= 21 and Mes_de_nacimiento == 6:
    print("Su Signo Zodiacal es Cancer")
elif dia_de_nacimiento <= 23 and Mes_de_nacimiento == 7:
    print("Su Signo Zodiacal es Cancer")
elif dia_de_nacimiento >= 23 and Mes_de_nacimiento == 7:
    print("Su Signo Zodiacal es Leo")
elif dia_de_nacimiento <= 23 and Mes_de_nacimiento == 8:
    print("Su Signo Zodiacal es Leo")
elif dia_de_nacimiento >= 23 and Mes_de_nacimiento == 8:
    print("Su Signo Zodiacal es Virgo")
elif dia_de_nacimiento <= 23 and Mes_de_nacimiento == 9:
    print("Su Signo Zodiacal es Virgo")
elif dia_de_nacimiento >= 23 and Mes_de_nacimiento == 9:
    print("Su Signo Zodiacal es Libra")
elif dia_de_nacimiento <= 23 and Mes_de_nacimiento == 10:
    print("Su Signo Zodiacal es Libra")
elif dia_de_nacimiento >= 23 and Mes_de_nacimiento == 10:
    print("Su Signo Zodiacal es Escorpio")
elif dia_de_nacimiento <= 22 and Mes_de_nacimiento == 11:
    print("Su Signo Zodiacal es Escorpio")
elif dia_de_nacimiento >= 23 and Mes_de_nacimiento == 11:
    print("Su Signo Zodiacal es Sagitario")
elif dia_de_nacimiento <= 22 and Mes_de_nacimiento == 12:
    print("Su Signo Zodiacal es Sagitario")
elif dia_de_nacimiento >= 22 and Mes_de_nacimiento == 12:
    print("Su Signo Zodiacal es Capricornio")
elif dia_de_nacimiento <= 20 and Mes_de_nacimiento == 1:
    print("Su Signo Zodiacal es Capricornio")
elif dia_de_nacimiento >= 20 and Mes_de_nacimiento == 1:
    print("Su Signo Zodiacal es Acuario")
elif dia_de_nacimiento <= 19 and Mes_de_nacimiento == 2:
    print("Su Signo Zodiacal es Acuario")
elif dia_de_nacimiento >= 19 and Mes_de_nacimiento == 2:
    print("Su Signo Zodiacal es Piscis")
elif dia_de_nacimiento <= 21 and Mes_de_nacimiento == 3:
    print("Su Signo Zodiacal es Piscis")
else:
    print("Datos mal ingresados")
