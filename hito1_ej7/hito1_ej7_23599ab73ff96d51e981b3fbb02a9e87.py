#Zodiaco
dia = int(input("Ingrese su día de nacimiento: "))
mes = int(input("Ingrese su mes de nacimiento: "))
if (mes==3):
    if (dia>=1 and dia<=20):
        print("Signo: Piscis")
    elif (dia>=21 and dia<=31):
        print("Signo: Aries")
elif (mes==4):
    if (dia>=1 and dia<=19):
        print("Signo: Aries")
    elif (dia>=20 and dia<=30):
        print("Signo: Tauro")
elif (mes==5):
    if (dia>=1 and dia<=20):
        print("Signo: Tauro")
    elif (dia>=21 and dia<=31):
        print("Signo: Géminis")
elif (mes==6):
    if (dia>=1 and dia<=21):
        print("Signo: Géminis")
    elif(dia>=22 and dia <=30):
        print("Signo: Cáncer")
elif (mes==7):
    if (dia>=1 and dia <=22):
        print("Signo: Cáncer")
    elif (dia>=23 and dia <=31):
        print("Signo: Leo")   
elif (mes==8):
     if (dia>=1 and dia <=23):
        print("Signo: Leo")
     elif (dia>=24 and dia <=31):
        print("Signo: Virgo")
elif (mes==9):
    if (dia>=1 and dia <=22):
        print("Signo: Virgo")
    elif(dia>=23 and dia <=30):
        print("Signo: Libra")   
elif (mes==10):
    if (dia>=1 and dia <=23):
        print("Signo: Libra")
    elif(dia>=24 and dia <=31):
        print("Signo: Escorpion")   
elif (mes==11):
    if (dia>=1 and dia <=22):
        print("Signo: Escorpion")
    elif(dia>=23 and dia <=30):
        print("Signo: Sagitario")
elif (mes==12):
    if (dia>=1 and dia <=22):
        print("Signo: Sagitario")
    elif(dia>=23 and dia <=31):
        print("Signo: Capricornio")
elif (mes==1):
    if (dia>=1 and dia <=20):
        print("Signo: Capricornio")
    elif(dia>=21 and dia <=31):
        print("Signo: Acuario")
elif (mes==2):
    if (dia>=1 and dia <=18):
        print("Signo: Acuario")
    elif(dia>=19 and dia <=29):
        print("Signo: Piscis")
else:
    print("Por favor, revise sus datos e intente de nuevo")      
        
      