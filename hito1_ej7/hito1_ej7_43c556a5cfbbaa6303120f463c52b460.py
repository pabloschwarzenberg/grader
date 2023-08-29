#Zodiaco
dia = input("Ingrese el DÍA de su cumpleaños: ")
mes = input("Ingrese el MES de su Cumpleaños: ")

d = str(dia)
m = str(mes)



print("Tu signo zodiacal es:\n")

if 1 <= int(m) < 2:
    if 1 <= int(d) <= 20:
        print("CAPRICORNIO")

    elif 21 <= d <= 31:
        print("ACUARIO")

    else:
        print("No se ingresó un día correcto")

elif 2 <= int(m) < 3:
    if 1 <= int(d) <= 19:
        print("ACUARIO")

    elif 20 <= int(d) <= 29:
        print("PISCIS")

    else:
        print("No se ingresó un día correcto")

elif 3 <= int(m) < 4:
    if  1 <= int(d) <= 20:
        print("PISCIS")

    elif 21 <= int(d) <= 31:
        print("ARIES")

    else:
        print("No se ingresó un día correcto")


elif 4 <= int(m) < 5:
    if  1 <= int(d) <= 20:
        print("ARIES")

    elif 21 <= int(d) <= 30:
        print("TAURO")

    else:
        print("No se ingresó un día correcto")

elif 5 <= int(m) < 6:
    if 1 <= int(d) <= 21:
        print("TAURO")

    elif 22 <= int(d) <= 31:
        print("GEMINIS")

    else:
        print("No se ingresó un día correcto")
elif 6 <= int(m) < 7:
    if  1 <= int(d) <= 21:
        print("GEMINIS")

    elif 22 <= int(d) <= 30:
        print("CANCER")

    else:
        print("No se ingresó un día correcto")

elif 7 <= int(m) < 8:
    if  1 <= int(d) <= 22:
        print("CANCER")

    elif 23 <= int(d) <= 31:
        print("LEO")

    else:
        print("No se ingresó un día correcto")

elif 8 <= int(m) < 9:
    if  1 <= int(d) <= 22:
        print("LEO")

    elif 23 <= int(d) <= 31:
        print("VIRGO")

    else:
        print("No se ingresó un día correcto")

elif 9 <= int(m) < 10:
    if  1 <= int(d) <= 23:
        print("VIRGO")

    elif 24<= int(d) <= 30:
        print("LIBRA")

    else:
        print("No se ingresó un día correcto")

elif 10 <= int(m) < 11:
    if 1 <= int(d) <= 23:
        print("LIBRA")

    elif 24 <= int(d) <= 31:
        print("ESCORPIÓN")

    else:
        print("No se ingresó un día correcto")

elif 11 <= int(m) < 12:
    if 1 <= int(d) <= 22:
        print("ESCORPIÓN")

    elif 23 <= int(d) <= 30:
        print("SAGITARIO")

    else:
        print("No se ingresó un día correcto")

elif 12 <= int(m) < 13:
    if  1 <= int(d) <= 21:
        print("SAGITARIO")

    elif 22<= int(d) <= 31:
        print("CAPRICORNIO")

    else:
        print("No se ingresó un día correcto")

