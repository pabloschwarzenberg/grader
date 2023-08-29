#Zodiaco
dia = int(input("ingrese su dia de nacimiento: "))
mes = int(input("ingrese su mes de nacimiento: "))

if(mes==3 or mes==4):
    if((mes==3 and dia>=21 and dia<=31) or (mes==4 and dia>=1 and dia<=20)):
        print("aries")

if(mes==4 or mes==5):
    if ((mes == 4 and dia >= 21 and dia <= 30) or (mes == 5 and dia >= 1 and dia <= 20)):
        print("tauro")

if(mes==5 or mes==6):
    if((mes==5 and dia>=21 and dia<=31) or (mes==6 and dia>=1 and dia<=21)):
        print("geminis")

if(mes==6 or mes==7):
    if ((mes == 6 and dia >= 22 and dia <= 30) or (mes == 7 and dia >= 1 and dia <= 22)):
        print("cancer")

if(mes==7 or mes==8):
    if((mes==7 and dia>=23 and dia<=31) or (mes==8 and dia>=1 and dia<=23)):
        print("leo")

if(mes==8 or mes==9):
    if ((mes == 8 and dia >= 24 and dia <= 31) or (mes == 9 and dia >= 1 and dia <= 22)):
        print("virgo")

if(mes==9 or mes==10):
    if((mes==9 and dia>=23 and dia<=30) or (mes==10 and dia>=1 and dia<=22)):
        print("libra")

if(mes==10 or mes==11):
    if ((mes == 10 and dia >= 23 and dia <= 31) or (mes == 11 and dia >= 1 and dia <= 22)):
        print("escorpio")

if(mes==11 or mes==12):
    if((mes==11 and dia>=23 and dia<=30) or (mes==12 and dia>=1 and dia<=21)):
        print("sagitario")

if(mes==12 or mes==1):
    if ((mes == 12 and dia >= 22 and dia <= 31) or (mes == 1 and dia >= 1 and dia <= 20)):
        print("capricornio")

if(mes==1 or mes==2):
    if((mes==1 and dia>=21 and dia<=31) or (mes==2 and dia>=1 and dia<=19)):
        print("acuario")

if(mes==2 or mes==3):
    if ((mes == 2 and dia >= 20 and dia <= 29) or (mes == 3 and dia >= 1 and dia <= 20)):
        print("piscis")