dia_nacimiento = int(input("Ingrese dia de nacimiento: "))
Mes_nacimiento = int(input("Ingres mes de nacimiento: "))

if dia_nacimiento >=21 and Mes_nacimiento >= 3 or dia_nacimiento <=20 and Mes_nacimiento <= 4:
    print("tu signo es aries")
elif dia_nacimiento >=21 and Mes_nacimiento >= 4 or dia_nacimiento <=21 and Mes_nacimiento <= 5:
    print("tu signo es tauro")
elif dia_nacimiento >=22 and Mes_nacimiento >= 5 or dia_nacimiento <=21 and Mes_nacimiento <= 6:
    print("tu signo es geminis")
elif dia_nacimiento >=22 and Mes_nacimiento >= 6 or dia_nacimiento <=22 and Mes_nacimiento <= 7:
    print("tu signo es cancer")
elif dia_nacimiento >=23 and Mes_nacimiento >= 7 or dia_nacimiento <=22 and Mes_nacimiento <= 8:
    print("tu signo es leo")
elif dia_nacimiento >=23 and Mes_nacimiento >= 8 or dia_nacimiento <=22 and Mes_nacimiento <= 9:
    print("tu signo es virgo")
elif dia_nacimiento >=23 and Mes_nacimiento >= 9 or dia_nacimiento <=22 and Mes_nacimiento <= 10:
    print("tu signo es libra")
elif dia_nacimiento >=23 and Mes_nacimiento >= 10 or dia_nacimiento <=22 and Mes_nacimiento <= 11:
    print("tu signo es escorpio")
elif dia_nacimiento >=23 and Mes_nacimiento >= 11 or dia_nacimiento <=21 and Mes_nacimiento <= 12:
    print("tu signo es sagitario")
elif dia_nacimiento >=21 and Mes_nacimiento >= 1 or dia_nacimiento <=19 and Mes_nacimiento <= 2:
    print("tu signo es acuario")
elif dia_nacimiento >=20 and Mes_nacimiento >= 2 or dia_nacimiento <=20 and Mes_nacimiento <= 3:
    print("tu signo es piscis")
else:
    print()