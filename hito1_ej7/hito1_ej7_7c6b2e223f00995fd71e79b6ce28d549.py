#Zodiaco
D=int(input("Día de Nacimiento:"))
M=int(input("Mes de Nacimiento:"))
if M==1:
    if D<21:
        print("CAPRICORNIO")
    else:
        print("ACUARIO")
elif M==2:
    if D<20:
        print("ACUARIO")
    else:
        print("PISCIS")
elif M==3:
    if D<21:
        print("PISCIS")
    else:
        print("ARIES")
elif M==4:
    if D<21:
        print("ARIES")
    else:
        print("TAURO")
elif M==5:
    if D<22:
        print("TAURO")
    else:
        print("GEMINIS")
elif M==6:
    if D<22:
        print("GEMINIS")
    else:
        print("CÁNCER")
elif M==7:
    if D<23:
        print("CÁNCER")
    else:
        print("LEO")
elif M==8:
    if D<23:
        print("LEO")
    else:
        print("VIRGO")
elif M==9:
    if D<24:
        print("VIRGO")
    else:
        print("LIBRA")
elif M==10:
    if D<24:
        print("LIBRA")
    else:
        print("ESCORPIÓN")
elif M==11:
    if D<23:
        print("ESCORPIÓN")
    else:
        print("SAGITARIO")
elif M==12:
    if D<22:
        print("SAGITARIO")
    else:
        print("CAPRICORNIO")