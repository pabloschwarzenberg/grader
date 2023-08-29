#Zodiaco
dia = int(input("Ingrese el dia: "))
mes = str(input("Ingrese su mes: "))


if mes=="3":
    if dia<21:
        print("Picis")
    if dia>=21:
        print("Aries")
if mes=="4":
    if dia<20:
        print("Aries")
    if dia>=20:
        print("Tauro")
if mes=="5":
    if dia<21:
        print("Tauro")
    if dia>=21:
        print("Geminis")
if mes=="6":
    if dia<21:
        print("Geminis")
    if dia>=21:
        print("Cancer")
if mes=="7":
    if dia<23:
        print("Cancer")
    if dia>=23:
        print("Leo")
if mes=="8":
    if dia<23:
        print("Leo")
    if dia>=23:
        print("Virgo")
if mes=="9":
    if dia<23:
        print("Virgo")
    if dia>23:
        print("Libra")
if mes=="10":
    if dia<23:
        print("Libra")
    if dia>23:
        print("Escorpio")
if mes=="11":
    if dia<22:
        print("Escorpio")
    if dia>=22:
        print("Sagitario")
if mes=="12":
    if dia<22:
        print("Sagitario")
    if dia>=22:
        print("Capricornio")
if mes=="1":
    if dia<20:
        print("Capricornio")
    if dia>=20:
        print("Acuario")
if mes=="2":
    if dia<19:
        print("Acuario")
    if dia>=19:
        print("Picis")

