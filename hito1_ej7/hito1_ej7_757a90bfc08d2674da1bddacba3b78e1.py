dia_nacimiento = int(input("ingrese dia de nacimiento: "))
mes_nacimiento = int(input("ingrese mes de nacimiento: "))
if mes_nacimiento == 1:
    if (dia_nacimiento <= 20) :
        print("capricornio")
    else:
        print("acuario")
if (mes_nacimiento == 2):
    if (dia_nacimiento >= 19):
        print("piscis") 
    else:
        print("acuario")
if (mes_nacimiento == 3):
    if (dia_nacimiento >= 21):
        print("aries")
    else:
        print("piscis")
if (mes_nacimiento == 4):
    if (dia_nacimiento >= 20):
        print("tauro")
    else:
        print("aries")
if (mes_nacimiento == 5):
    if (dia_nacimiento >= 21):
        print("geminis")
    else:
        print("tauro")
if (mes_nacimiento == 6):
    if (dia_nacimiento >= 21):
        print("cancer")
    else:
        print("geminis")
if (mes_nacimiento == 7):
    if (dia_nacimiento >= 23):
        print("leon")
    else:
        print("cancer")
if (mes_nacimiento == 8):
    if (dia_nacimiento >= 23):
        print("virgo")
    else:
        print("leon")
if (mes_nacimiento == 9):
    if (dia_nacimiento >= 23):
        print("libra")
    else:
        print("virgo")
if (mes_nacimiento == 10):
    if (dia_nacimiento >= 23):
        print("escorpio")
    else:
        print("libra")
if (mes_nacimiento == 11):
    if (dia_nacimiento >= 23):
        print("sagitario")
    else:
        print("escorpio")
if (mes_nacimiento == 12):
    if (dia_nacimiento >= 22):
        print("capricornio")
    else:
        print("sagitario")