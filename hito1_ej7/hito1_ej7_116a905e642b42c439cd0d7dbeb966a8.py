#Zodiaco
dia_nacimiento=int(input("Ingrese dia de nacimiento: "))
mes_nacimiento=int(input("Ingrese mes de nacimiento: "))

if mes_nacimiento == 1:
    if dia_nacimiento <= 20:
        print("Capricornio")
    else:
        print("Acuario")
elif mes_nacimiento == 2:
    if dia_nacimiento <= 18:
        print("Acuario")
    else:
        print("Piscis")
elif mes_nacimiento == 3:
    if dia_nacimiento <= 20:
        print("Piscis")
    else:
        print("Aries")
elif mes_nacimiento == 4:
    if dia_nacimiento <= 20:
        print("Aries")
    else:
        print("Tauro")
elif mes_nacimiento == 5:
    if dia_nacimiento <= 21:
        print("Tauro")
    else:
        print("Geminis")
elif mes_nacimiento == 6:
    if dia_nacimiento <= 21:
        print("Geminis")
    else:
        print("Cancer")
elif mes_nacimiento == 7:
    if dia_nacimiento <= 22:
        print("Cáncer")
    else:
        print("Leo")
elif mes_nacimiento == 8:
    if dia_nacimiento <= 23:
        print("Leo")
    else:
        print("Virgo")
elif mes_nacimiento == 9:
    if dia_nacimiento <= 23:
        print("Virgo")
    else:
        print("Libra")
elif mes_nacimiento == 10:
    if dia_nacimiento <= 23:
        print("Libra")
    else:
        print("Escorpio")
elif mes_nacimiento == 11:
    if dia_nacimiento <= 22:
        print("Escorpio")
    else:
        print("Sagitario")
elif mes_nacimiento == 12:
    if dia_nacimiento <= 21:
        print("Sagitario")
    else:
        print("Capricornio")
        