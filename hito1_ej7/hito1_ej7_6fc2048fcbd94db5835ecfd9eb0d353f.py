#Zodiaco
dia=int(input("Ingrese el dia del cumpleaños de la persona:"))
mes= int(input("Ingrese el numero del mes de cumpleaños de la persona:"))
if dia>=21 and mes==3 or dia<20 and mes==4:
    print("La persona es Aries")
elif dia>=20 and mes==4 or dia<21 and mes==5:
    print("La persona es Tauro")
elif dia>=21 and mes==5 or dia<21 and mes==6:
    print("La persona es Geminis")
elif dia>=21 and mes==6 or dia<23 and mes==7:
    print("La persona es Cancer")
elif dia>=23 and mes==7 or dia<23 and mes==8:
    print("La personas es Leo")
elif dia>=23 and mes==8 or dia<23 and mes==9:
    print("La persona es Virgo")
elif dia>=23 and mes==9 or dia<23 and mes==10:
    print("La personas es Libra")
elif dia>=23 and mes==10 or dia<22 and mes==11:
    print("La persona es Escorpio")
elif dia>=22 and mes==11 or dia<22 and mes==12:
    print("La persona es Sagitario")
elif dia>=22 and mes==12 or dia<20 and mes==1:
    print("La persona es Capricornio")
elif dia>=20 and mes==1 or dia<19 and mes==2:
    print("La persona es Acuario")
else:
    dia>=19 and mes==2 or dia<21 and mes==3
    print("La persona es Piscis")