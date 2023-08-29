dia=int(input("Ingrese su día de nacimiento:"))
mes=int(input("Ingrese su mes de cumpleaños:"))
if (mes==11 and dia>=22 and dia<=30) or (mes==12 and dia>=1 and dia<22):
    print("sagitario")
elif (mes==12 and dia>=22 and dia<=31) or (mes==1 and dia>=1 and dia<20):
    print("capricornio")
elif (mes==1 and dia>=20 and dia<=31) or (mes==2 and dia>=1 and dia<19):
    print("acuario")
elif (mes==2 and dia>=19 and dia<=29) or (mes==3 and dia>=1 and dia<21):
    print("piscis")
elif (mes==3 and dia>=21 and dia<=31) or (mes==4 and dia>=1 and dia<20):
    print("aries")
elif (mes==4 and dia>=20 and dia<=30) or (mes==5 and dia>=1 and dia<21):
    print("tauro")
elif (mes==5 and dia>=21 and dia<=31) or (mes==6 and dia>=1 and dia<21):
    print("geminis")
elif (mes==6 and dia>=21 and dia<=31) or (mes==7 and dia>=1 and dia<23):
    print("cancer")
elif (mes==7 and dia>=23 and dia<=31) or (mes==8 and dia>=1 and dia<23):
    print("Leo")
elif (mes==8 and dia>=23 and dia<=30) or (mes==9 and dia>=1 and dia<23):
    print("virgo")
elif (mes==9 and dia>=23 and dia<=30) or (mes==10 and dia>=1 and dia<23):
    print("libra")
elif (mes==10 and dia>=23 and dia<=31) or (mes==11 and dia>=1 and dia<22):
    print("escorpio")
else:print("ophiuchus")