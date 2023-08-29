#Zodiaco
a1=int(input("Día: "))
a2=int(input("Mes: "))
if a2==1:
    if a1<=19:
        print("capricornio")
    else:
        print("acuario")
elif a2==2:
    if a1<=18:
        print("acuario")
    else:
        print("piscis")
elif a2==3:
    if a1>=21:
        print("aries")
    else:
        print("piscis")
elif a2==4:
    if a1<=20:
        print("aries")
    else:
        print("tauro")
elif a2==5:
    if a1<=20:
        print("tauro")
    else:
        print("géminis")
elif a2==6:
    if a1<=20:
        print("géminis")
    else:
        print("cáncer")
elif a2==7:
    if a1<=20:
        print("cáncer")
    else:
        print("leo")
elif a2==8:
    if a2<=21:
        print("leo")
    else:
        print("virgo")
elif a2==9:
    if a2<=22:
        print("virgo")
    else:
        print("libra")
elif a2==10:
    if a2<=22:
        print("libra")
    else:
        print("escorpio")
elif a2==11:
    if a2<=22:
        print("escorpio")
    else:
        print("sagitario")
else:
    if a2<=20:
        print("sagitario")
    else:
        print("capricornio")