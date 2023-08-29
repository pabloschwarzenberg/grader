#Zodiaco
dia=int(input("ingrese dia de nacimiento:"))
mes=int(input("ingrese mes de nacimiento:"))

if (dia>=21 and dia<=31 and mes==3) or (dia>0 and dia<=20 and mes==4):
    print("tu signo del zodiaco es ARIES")
    
elif (dia>=21 and dia<=30 and mes==4) or (dia>0 and dia<=21 and mes==5):
    print("tu signo del zodico es TAURO")

elif (dia>=22 and dia<=31 and mes==5) or (dia>0 and dia<=21 and mes==6):
    print("tu signo del zodiaco es GEMINIS")

elif (dia>=22 and dia<=30 and mes==6) or (dia>0 and dia<=22 and mes==7):
    print("tu signo del zodiaco es CANCER")

elif (dia>=23 and dia<=31 and mes==7) or (dia>0 and dia<=23 and mes==8):
    print("tu signo del zodiaco es LEO")

elif (dia>=23 and dia<=31 and mes==8) or (dia>0 and dia<=23 and mes==9):
    print("tu signo del zodiaco es VIRGO")

elif (dia>=24 and dia<=30 and mes==9) or (dia>0 and dia<=23 and mes==10):
    print("tu signo del zodiaco es LIBRA")

elif (dia>=24 and dia<=31 and mes==10) or (dia>0 and dia<=22 and mes==11):
    print("tu signo del zodiaco es ESCORPION")

elif (dia>=23 and dia<=30 and mes==11) or (dia>0 and dia<=21 and mes==12):
    print("tu signo del zodiaco es SAGITARIO")

elif (dia>=22 and dia<=31 and mes==12) or (dia>0 and dia<=20 and mes==1):
    print("tu signo del zodiaco es CAPRICORNIO")

elif (dia>=21 and dia<=31 and mes==1) or (dia>0 and dia<=19 and mes==2):
    print("tu signo del zodiaco es ACUARIO")

elif(dia>=20 and dia<=29 and mes==2) or (dia>0 and dia<=20 and mes==3):
    print("tu signo del zodiaco es PISCIS")

else:
    print("dia o mes de nacimiento incorrectos")

     