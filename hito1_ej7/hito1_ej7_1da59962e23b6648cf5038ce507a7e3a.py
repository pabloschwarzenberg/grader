#Zodiaco
dia=int(input("Ingrese el número de su día de nacimiento: "))
mes=int(input("Ingrese el número de su mes de nacimiento: "))
if mes==3 and (dia>=21 and dia<=31) or mes==4 and dia<=20:
    print("Usted es Aries")
elif mes==4 and (dia>=21 and dia<=30) or mes==5 and dia<=21:
    print("Usted es Tauro")
elif mes==5 and (dia>=22 and dia<=31) or mes==6 and dia<=21:
    print("Usted es Geminis")
elif mes==6 and (dia>=22 and dia<=30) or mes==7 and dia<=23:
    print("Usted es Cancer")
elif mes==7 and (dia>=24 and dia<=31) or mes==8 and dia<=23:
    print("Usted es Leo")
elif mes==8 and (dia>=24 and dia<=31) or mes==9 and dia<=23:
    print("Usted es Virgo")
elif mes==9 and (dia>=24 and dia<=30) or mes==10 and dia<=23:
    print("Usted es Libra")
elif mes==10 and (dia>=24 and dia<=31) or mes==11 and dia<=22:
    print("Usted es Escorpio")
elif mes==11 and (dia>=23 and dia<=30) or mes==12 and dia<=22:
    print("Usted es Sagitario")
elif mes==12 and (dia>=23 and dia<=31) or mes==1 and dia<=20:
    print("Usted es Capricornio")
elif mes==1 and (dia>=21 and dia<=31) or mes==2 and dia<=19:
    print("Usted es Acuario")
elif mes==2 and (dia>=20 and dia<=29) or mes==3 and dia<=20:
    print("Usted es Picis")      