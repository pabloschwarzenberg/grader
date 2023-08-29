#Zodiaco

día_nacimiento = int(input("Ingrese dia de nacimiento: "))
Mes_nacimiento = int(input("Ingres mes de nacimiento: "))

if día_nacimiento >=21 and Mes_nacimiento >= 3 or día_nacimiento <=20 and Mes_nacimiento <= 4:
    print("tu signo es aries")
elif día_nacimiento >=21 and Mes_nacimiento >= 4 or día_nacimiento <=21 and Mes_nacimiento <= 5:
    print("tu signo es tauro")
elif día_nacimiento >=22 and Mes_nacimiento >= 5 or día_nacimiento <=21 and Mes_nacimiento <= 6:
    print("tu signo es geminis")
elif día_nacimiento >=22 and Mes_nacimiento >= 6 or día_nacimiento <=22 and Mes_nacimiento <= 7:
    print("tu signo es cancer")
elif día_nacimiento >=23 and Mes_nacimiento >= 7 or día_nacimiento <=22 and Mes_nacimiento <= 8:
    print("tu signo es leo")
elif día_nacimiento >=23 and Mes_nacimiento >= 8 or día_nacimiento <=22 and Mes_nacimiento <= 9:
    print("tu signo es virgo")
elif día_nacimiento >=23 and Mes_nacimiento >= 9 or día_nacimiento <=22 and Mes_nacimiento <= 10:
    print("tu signo es libra")
elif día_nacimiento >=23 and Mes_nacimiento >= 10 or día_nacimiento <=22 and Mes_nacimiento <= 11:
    print("tu signo es escorpio")
elif día_nacimiento >=23 and Mes_nacimiento >= 11 or día_nacimiento <=21 and Mes_nacimiento <= 12:
    print("tu signo es sagitario")
elif día_nacimiento >=21 and Mes_nacimiento >= 1 or día_nacimiento <=19 and Mes_nacimiento <= 2:
    print("tu signo es acuario")
elif día_nacimiento >=20 and Mes_nacimiento >= 2 or día_nacimiento <=20 and Mes_nacimiento <= 3:
    print("tu signo es piscis")
else:
    print()
      