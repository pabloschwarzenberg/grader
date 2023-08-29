dia = int(input("Ingrese dia de nacimiento: "))
mes = int(input("Ingrese mes de nacimiento (en formato numeros): "))

if mes == 1:
    if dia < 20:
        print("capricornio")
    else:
        print("acuario")
if mes == 2:
    if dia < 19:
        print("acuario")
    else:
        print("picis")
if mes == 3:
    if dia < 21:
        print("picis")
    else:
        print("aries")
if mes == 4:
    if dia < 20:
        print("aries")
    else:
        print("tauro")
if mes == 5:
    if dia < 21:
        print("tauro")
    else:
        print("geminis")
if mes == 6:
    if dia < 21:
        print("geminis")
    else:
        print("cancer")
if mes == 7:
    if dia < 23:
        print("cancer")
    else:
        print("leo")
if mes == 8:
    if dia < 23:
        print("leo")
    else:
        print("virgo")
if mes == 9:
    if dia < 23:
        print("virgo")
    else:
        print("libra")
if mes == 10:
    if dia < 23:
        print("libra")
    else:
        print("scorpio")
if mes == 11:
    if dia <= 22:
        print("scorpio")
    else:
        print("sagitario")
if mes == 12:
    if dia < 22:
        print("sagitario")
    else:
        print("capricornio")

      