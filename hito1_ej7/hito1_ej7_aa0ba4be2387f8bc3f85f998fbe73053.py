#Zodiaco
dia= int(input("INGRESA TU DIA DE NACIMIENTO: "))
mes=int(input("INGRESA TU MES DE NACIMIENTO: "))

if(mes==1):
    if(dia>20):
        print("acuario")

elif(mes==2):
    if(dia<19):
        print("acuario")
    else:
        print("piscis")
elif(mes==3):
    if(dia<21):
        print("piscis")
    else:
        print("aries")
elif(mes==4):
    if(dia<20):
        print("aries")
    else:
        print("tauro")
elif(mes==5):
    if(dia<21):
        print("tauro")
    else:
        print("geminis")
elif(mes==6):
    if(dia<21):
        print("geminis")
    else:
        print("cancer")
elif(mes==7):
    if(dia<23):
        print("cancer")
    else:
        print("leo")
elif(mes==8):
    if(dia<23):
        print("leo")
    else:
        print("virgo")
elif(mes==9):
    if(dia<23):
        print("virgo")
    else:
        print("su signo del zodiaco es libra")
elif(mes==10):
    if(dia<23):
        print("libra")
    else:
        print("escorpio")
elif(mes==11):
    if(dia<23):
        print("escorpio")
    else:
        print("sagitario")
elif(mes==12):
    if(dia<22):
        print("sagitario")
    else:
        print("acuario")
