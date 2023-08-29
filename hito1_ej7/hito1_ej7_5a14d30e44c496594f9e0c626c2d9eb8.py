#Zodiaco
dia = int(input("Ingrese dia: "))
mes = int(input("Ingrese mes: "))

if mes == 3:
    if dia >= 21 and dia <=31:
        print("Aries")
    else:
        print("Piscis")
elif mes == 4:
    if(dia >=20 and dia<=30):
        print("Tauro")
    else:
        print("Aries")
elif mes ==5:
    if(dia >= 21 and dia <=31):
        print("Geminis")
    else:
        print("Tauro")
elif mes == 6:
    if(dia >=21 <=30):
        print("Cancer")
    else:
        print("Geminis")
elif mes == 7:
    if dia >= 23 and dia <=31:
        print("Leo")
    else:
        print("Cancer")
elif mes == 8:
    if dia >=23 and dia <= 31:
        print("Virgo")
    else:
        print("Leo")
elif mes == 9:
    if dia >= 23 and dia <= 30:
        print("Libra")
    else:
        print("Virgo")
elif mes == 10:
    if dia >= 23 and dia <= 31:
        print("Escorpio")
    else:
        print("Libra")
elif mes == 11:
    if dia >= 23 and dia <= 30:
        print("Sagitario")
    else:
        print("Escorpio")
elif mes == 12:
    if dia >= 22 and dia <= 31:
        print("Capricornio")
    else:
        print("Sagitario")
elif mes == 1:
    if dia >= 20 and dia <=31:
        print("Acuario")
    else:
        print("Capricornio")
elif mes == 2:
    if dia >= 19 and dia <=29:
        print("Piscis")
    else:
        print("Acuario")     