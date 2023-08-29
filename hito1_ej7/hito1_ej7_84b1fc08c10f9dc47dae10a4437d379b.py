dia = int(input("Ingrese su dia de cumpleaños: "))
mes = int(input("Ingrese su mes de cumpleaños: "))

if mes == 1:
    if dia < 20:
        print("capricornio")
    else:
        print("acuario")
elif mes == 2:
    if dia < 19:
        print("acuario")
    else:
        print("aries")
elif mes == 3:
    if dia > 21:
        print("aries")
    else:
        print("picsis")
elif mes == 4:
    if dia < 20:
        print("aries")
    else:
        print("tauro")
elif mes == 5:
    if dia < 21:
        print("tauro")
    else:
        print("geminis")
elif mes == 6:
    if dia < 21:
        print("geminis")
    else:
        print("cancer")
elif mes == 7:
    if dia < 21:
        print("cancer")
    else:
        print("leo")
elif mes == 8:
    if dia < 23:
        print("leo")
    else:
        print("virgo")
elif mes == 9:
    if dia < 23:
        print("virgo")
    else:
        print("libra")
elif mes == 10:
    if dia < 23:
        print("libra")
    else:
        print("escorpio")
elif mes == 11:
    if dia < 23:
        print("escorpio")
    else:
        print("sagitario")
else:
    if dia < 22:
        print("sagitario")
    else:
        print("capricornio")