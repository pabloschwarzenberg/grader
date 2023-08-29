#Zodiaco
dia=int(input("Ingrese dia de nacimiento: "))
mes=int(input("Ingrese mes de nacimiento: "))

if mes==1:
    if dia<21:
        print("Capricornio")
    else:
        print("Acuario")
if mes==2:
    if dia<20:
        print("Acuario")
    else:
        print("Piscis")
if mes==3:
    if dia<21:
        print("Piscis")
    else:
        print("Aries")
if mes==4:
    if dia<21:
        print("Aries")
    else:
        print("Tauro")
if mes==5:
    if dia<22:
        print("Tauro")
    else:
        print("Geminis")
if mes==6:
    if dia<22:
        print("Geminis")
    else:
        print("Cancer")
if mes==7:
    if dia<23:
        print("Cancer")
    else:
        print("Leo")
if mes==8:
    if dia<23:
        print("Leo")
    else:
        print("Virgo")
if mes==9:
    if dia<24:
        print("Virgo")
    else:
        print("Libra")
if mes==10:
    if dia<24:
        print("Libra")
    else:
        print("Escorpio")
if mes==11:
    if dia<23:
        print("Escorpio")
    else:
        print("Sagitario")
if mes==12:
    if dia<22:
        print("Sagitario")
    else:
        print("Capricornio")
else:
    print("error")