#Zodiaco
dia_nacimiento = int(input("Ingrese su dia de nacimiento: "))
mes_nacimiento = int(input("Ingrese su mes de nacimiento: "))

#Procedimiento
if dia_nacimiento >= 21 and mes_nacimiento == 3 or dia_nacimiento <= 20 and mes_nacimiento == 4:
    print("Su signo es Aries")
elif dia_nacimiento >= 20 and mes_nacimiento == 4 or dia_nacimiento <= 21 and mes_nacimiento == 5:
    print("Su signo es Tauro")
elif dia_nacimiento >= 21 and mes_nacimiento == 5 or dia_nacimiento <= 21 and mes_nacimiento == 6:
    print("Su signo es Geminis")
elif dia_nacimiento >= 21 and mes_nacimiento == 6 or dia_nacimiento <= 23 and mes_nacimiento == 7:
    print("Su signo es Cáncer")
elif dia_nacimiento >= 23 and mes_nacimiento == 7 or dia_nacimiento <= 23 and mes_nacimiento == 8:
    print("Su signo es Leo")
elif dia_nacimiento >= 23 and mes_nacimiento == 8 or dia_nacimiento <= 23 and mes_nacimiento == 9:
    print("Su signo es Virgo")
elif dia_nacimiento >= 23 and mes_nacimiento == 9 or dia_nacimiento <= 23 and mes_nacimiento == 10:
    print("Su signo es Libra")
elif dia_nacimiento >= 23 and mes_nacimiento == 10 or dia_nacimiento <= 22 and mes_nacimiento == 11:
    print("Su signo es Escorpio")
elif dia_nacimiento >= 23 and mes_nacimiento == 11 or dia_nacimiento <= 22 and mes_nacimiento == 12:
    print("Su signo es Sagitario")
elif dia_nacimiento >= 22 and mes_nacimiento == 12 or dia_nacimiento <= 20 and mes_nacimiento == 1:
    print("Su signo es Capricornio")
elif dia_nacimiento >= 20 and mes_nacimiento == 1 or dia_nacimiento <= 19 and mes_nacimiento == 2:
    print("Su signo es Acuario")
else:
    print("Su signo es Piscis")