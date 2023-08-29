#Zodiaco
dia=int(input("ingrese dia de cumpleaños:"))
mes=int(input("ingrese mes de cumpleaños con numero:"))
if mes==3 and dia>=21 and dia<=31:
    print("Aries")
elif dia<=19 and dia>=1 and mes==4:
    print("Aries")
elif dia<=30 and dia>=20 and mes==4: 
    print("Tauro")
elif dia<=20 and dia>=1 and mes==5:
    print("Tauro")
elif dia<=31 and dia>=21 and mes==5:
    print("Geminis")
elif dia<=20 and dia>=1 and mes==6:
    print("Geminis")
elif dia<=30 and dia>=21 and mes==6:
    print("Cancer")
elif dia<=22 and dia>=1 and mes==7:
    print("Cancer")
elif dia<=31 and dia>=23 and mes==7:
    print("Leo")
elif dia<=22 and dia>=1 and mes==8:
    print("Leo")
elif dia<=31 and dia>=23 and mes==8:
    print("Virgo")
elif dia<=22 and dia>=1 and mes==9:
    print("Virgo")
elif dia<=30 and dia>=23 and mes==9: 
    print("Libra")
elif dia<=22 and dia>=1 and mes==10:
    print("Libra")
elif dia<=31 and dia>= 23 and mes==10:
    print("Escorpio")
elif dia<=21 and dia>=1 and mes==11:
    print("Escorpio")
elif dia<=30 and dia>=23 and mes==11:
    print("Sagitario")
elif dia<=21 and dia>=1 and mes==12:
    print("Sagitario")
elif dia<=31 and dia>=22 and mes==12: 
    print("Capricornio")
elif dia<=19 and dia>=1 and mes==1:
    print("Capricornio")
elif dia<=31 and dia>=20 and mes==1:
    print("Acuario")
elif dia<=18 and dia>=1 and mes==2:
    print("Acuario")
elif dia<=31 and dia>=19 and mes==2: 
    print("Picis")
elif dia<=20 and dia>=1 and mes==3:
    print("Picis")
else:
    print("No valido")