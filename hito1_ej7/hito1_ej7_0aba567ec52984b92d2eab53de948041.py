numero_dia = int(input("Coloque el dia: "))
numero_mes =(input("Coloque su mes: "))


if numero_mes=="3":
    if numero_dia<21:
        print("Picis")
    if numero_dia>=21:
        print("Aries")
if numero_mes=="4":
    if numero_dia<20:
        print("Aries")
    if numero_dia>=20:
        print("Tauro")
if numero_mes=="5":
    if numero_dia<21:
        print("Tauro")
    if numero_dia>=21:
        print("Geminis")
if numero_mes=="6":
    if numero_dia<21:
        print("Geminis")
    if numero_dia>=21:
        print("Cancer")
if numero_mes=="7":
    if numero_dia<23:
        print("Cancer")
    if numero_dia>=23:
        print("Leo")
if numero_mes=="8":
    if numero_dia<23:
        print("Leo")
    if numero_dia>=23:
        print("Virgo")
if numero_mes=="9":
    if numero_dia<23:
        print("Virgo")
    if numero_dia>23:
        print("Libra")
if numero_mes=="10":
    if numero_dia<23:
        print("Libra")
    if numero_dia>23:
        print("Escorpio")
if numero_mes=="11":
    if numero_dia<22:
        print("Escorpio")
    if numero_dia>=22:
        print("Sagitario")
if numero_mes=="12":
    if numero_dia<22:
        print("Sagitario")
    if numero_dia>=22:
        print("Capricornio")
if numero_mes=="1":
    if numero_dia<20:
        print("Capricornio")
    if numero_dia>=20:
        print("Acuario")
if numero_mes=="2":
    if numero_dia<19:
        print("Acuario")
    if numero_dia>=19:
        print("Picis")
else:
    print("numero invalido")
