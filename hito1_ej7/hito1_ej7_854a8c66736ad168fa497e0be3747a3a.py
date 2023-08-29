#Zodiaco
dia=int(input("Ingrese día de nacimiento: "))
mes=int(input("Ingrese mes de nacimiento: "))

if mes==3 and (dia>=21 and dia<=31) or mes==4 and (dia>=1 and dia<=20):
    print("Aries")

elif mes==4 and (dia>=21 and dia<=30) or mes==5 and (dia>=1 and dia<=20):
    print("Tauro")

elif mes==5 and (dia>=21 and dia<=31) or mes==6 and (dia>=1 and dia<=21):
    print("Géminis")

elif mes==6 and (dia>=22 and dia<=30) or mes==7 and (dia>=1 and dia<=22):
    print("cancer")

elif mes==7 and (dia>=23 and dia<=31) or mes==8 and (dia>=1 and dia<=22):
    print("Leo")

elif mes==8 and (dia>=23 and dia<=31) or mes==9 and (dia>=1 and dia<=22):
    print("Virgo")

elif mes==9 and (dia>=23 and dia<=30) or mes==10 and (dia>=1 and dia<=22):
    print("Libra")

elif mes==10 and (dia>=23 and dia<=31) or mes==11 and (dia>=1 and dia<=22):
    print("Escorpio")

elif mes==11 and (dia>=23 and dia<=30) or mes==12 and (dia>=1 and dia<=21):
    print("Sagitario")

elif mes==12 and (dia>=22 and dia<=31) or mes==1 and (dia>=1 and dia<=20):
    print("Capricornio")

elif mes==1 and (dia>=21 and dia<=31) or mes==2 and (dia>=1 and dia<=18):
    print("Acuario")

elif mes==2 and (dia>=19 and dia<=29) or mes==3 and (dia>=1 and dia<=20):
    print("Piscis")
else:
    print("No posee signo zodiacal")