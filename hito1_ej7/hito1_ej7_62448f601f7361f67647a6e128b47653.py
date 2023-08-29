#Zodiaco
print("Ingrese su fecha de nacimiento")
dia = int(input("Día: "))
mes = str(input("Mes en número: "))

if mes == "3":
    if dia < 21:
        print("Piscis")
    elif dia >= 21:
        print("Aries")
elif mes == "4":
    if dia < 20:
        print("Aries")
    elif dia >= 20:
        print("Tauro")
elif mes == "5":
    if dia < 21:
        print("Tauro")
    elif dia >= 21:
        print("Geminis")
elif mes == "6":
    if dia < 21:
        print("Geminis")
    elif dia >= 21:
        print("Cáncer")
elif mes == "7":
    if dia < 23:
        print("Cáncer")
    elif dia >= 23:
        print("Leo")
elif mes == "8":
    if dia < 23:
        print("Leo")
    elif dia >= 23:
        print("Virgo")
elif mes == "9":
    if dia < 23:
        print("Virgo")
    elif dia >= 23:
        print("Libra")
elif mes == "10":
    if dia < 23:
        print("Libra")
    elif dia >= 23:
        print("Escorpio")
elif mes == "11":
    if dia < 22:
        print("Escorpio")
    elif dia >= 22:
        print("Sagitario")
elif mes == "12":
    if dia < 22:
        print("Sagitario")
    elif dia >= 22:
        print("Capricornio")
elif mes == "1":
    if dia < 20:
        print("Capricornio")
    elif dia >= 20:
        print("Acuario")
    elif mes == "2":
        if dia < 19:
            print("Acuario")
        elif dia >= 19:
            print("Piscis")
