#Zodiaco
numero1=int(input("ingrese su dia de nacimeinto"))
numero2=int(input("ingrese su mes de nacimeinto"))
if(numero1>=21 and numero1<=31 and numero2==3):
    print("aries")
elif(numero1>=1 and numero1<=20 and numero2==4):
    print("aries")
elif(numero1>=21 and numero1<=30 and numero2==4):
    print("tauro")
elif(numero1>=1 and numero1<=21 and numero2==5):
    print("tauro")
elif(numero1>=22 and numero1<=31 and numero2==5):
    print("geminis")
elif(numero1>=1 and numero1<=21 and numero2==6):
    print("geminis")
elif(numero1>=22 and numero1<=31 and numero2==6):
    print("cancer")
elif(numero1>=1 and numero1<=22 and numero2==7):
    print("cancer")
elif(numero1>=23 and numero1<=31 and numero2==7):
    print("leo")
elif(numero1>=1 and numero1<=23 and numero2==8):
    print("leo")
elif(numero1>=24 and numero1<=31 and numero2==8):
    print("virgo")
elif(numero1>=1 and numero1<=23 and numero2==9):
    print("virgo")
elif(numero1>=24 and numero1<=31 and numero2==9 ):
    print("libra")
elif(numero1>=1 and numero1<=23 and numero2==10):
    print("libra")
elif(numero1>=24 and numero1<=31 and numero2==10 ):
    print("escorpio")
elif(numero1>=1 and numero1<=22 and numero2==11):
    print("escorpio")
elif(numero1>=23 and numero1<=31 and numero2==11 ):
    print("sagitario")
elif(numero1>=1 and numero1<=21 and numero2==12):
    print("sagitario")
elif(numero1>=22 and numero2<=31 and numero2==12):
    print("capricornio")
elif(numero1>=1 and numero1<=20 and numero2==1):
    print("capricornio")
elif(numero1>=21 and numero1<=31 and numero2==1):
    print("acuario")
elif(numero1>=1 and numero1<=18and numero2==2):
    print("acuario")
elif(numero1>=19 and numero1<=31 and numero2==2):
    print("piscis")
elif(numero1>=1 and numero1<=20 and numero2==3):
    print("piscis")
else:
    print("los numeros ingresados no corresponden a ningun dia o mes del año")