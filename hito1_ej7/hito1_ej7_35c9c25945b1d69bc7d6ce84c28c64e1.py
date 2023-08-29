#Zodiaco
dia = int(input("ingrese su dia de nacimiento(numero)= "))
mes = int(input("ingrese el mes de nacimiento= "))

if mes == 3:
    if dia <= 20:
       print("PISCIS")
    else:
       print("ARIES")
elif mes == 4:
    if dia <= 19:
        print("ARIES")
    else:
        print("TAURO")
elif mes == 5:
    if dia <= 20:
        print("TAURO")
    else:
        print("GÉMINIS")
elif mes == 6:
    if dia <= 20:
        print("GÉMINIS")
    else:
        print("CANCER")
elif mes == 7:
    if dia <= 22:
        print("CANCER")
    else:
        print("LEO")
elif mes == 8:
    if dia <= 22:
        print("LEO")
    else:
        print("VIRGO")
elif mes == 9:
    if dia <= 22:
        print("VIRGO")
    else:
        print("LIBRA")
elif mes == 10:
    if dia <= 22:
        print("LIBRA")
    else:
        print("ESCORPIO")
elif mes == 11:
    if dia <= 21:
        print("ESCORPIO")
    else:
        print("SAGITARIO")
elif mes == 12:
    if dia <= 21:
        print("SAGITARIO")
    else:
        print("CAPRICORNIO")
elif mes == 1:
    if dia <= 19:
        print("CAPRICORNIO")
    else:
        print("ACUARIO")
elif mes == 2:
    if dia <= 18:
        print("ACUARIO")
    else:
        print("PISCIS")
else:
    print("DATOS INVALIDOS")
    

      