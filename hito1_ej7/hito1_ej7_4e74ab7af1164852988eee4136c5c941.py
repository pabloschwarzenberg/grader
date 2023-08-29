dia = int(input("Ingrese dia de nacimiento:"))
mes = int(input("Ingrese mes de nacimiento:"))

if mes == 3:
    if dia <=21:
        print("Piscis")
    elif dia >=21 and dia<=31:
        print("Aries")

elif mes == 4:
    if dia>=1 and dia<=20:
        print("Aries")
    elif dia>=20 and dia<=30:
        print("Tauro")

elif mes == 5:
    if dia >=1 and dia <=21:
        print("Tauro")
    elif dia >=21 and dia<=31:
        print("Geminis")

elif mes == 6:
    if dia <=21:
        print("Geminis")
    elif dia >=21 and dia <=30:
        print("Cancer")

elif mes == 7:
    if dia <=23:
        print("Cancer")
    elif dia >=23 and dia <=31:
        print("Leo")

elif mes == 8:
    if dia <=23:
        print("Leo")
    if dia >=23 and dia <=31:
        print("Virgo")

elif mes == 9:
    if dia <=23:
        print("Virgo")
    elif dia >=23 and dia <=30:
        print("Libra")

elif mes == 10:
    if dia <=23:
        print("Libra")
    elif dia >= 23 and dia <=31:
        print("Escorpion")

elif mes == 11:
    if dia<=22:
        print("Escorpion")
    elif dia >=23 and dia <=30:
        print("Sagitario")

elif mes == 12:
    if dia <=22:
        print("Sagitario")
    elif dia >=22 and dia <=31:
        print("Capricornio")

elif mes == 1:
    if dia <=20:
        print("Capricornio")
    elif dia >=20 and dia <=31:
        print("Acuario")

elif mes == 2:
    if dia <=19:
        print("Acuario")
    elif dia >=19 and dia <=28:
        print("Piscis")