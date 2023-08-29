#Zodiaco

dia = int(input("ingrese número de día:"))
while not(dia<32 and dia>0):
     dia = int(input("ingrese un número valido de día:"))
mes = int(input("ingrese número de mes:"))
while not(mes<13 and mes>0):
    mes = int(input("ingrese un número valido de mes:"))

if(dia>=20 and mes>=4):
    if(dia<21 and mes<=3):
        print("Aries")
elif(dia>=21 and mes>=5):
    if(dia<20 and mes<=4):
        print("Tauro")
elif(dia>=21 and mes>=6):
    if(dia<21 and mes<=5):
        print("Geminis")
elif(dia>=23 and mes>=7):
    if(dia<21 and mes<=6):
        print("Cancer")
elif(dia>=23 and mes>=8):
    if(dia<23 and mes<=7):
        print("Leo")
elif(dia>=23 and mes>=9):
    if(dia<23 and mes<=8):
        print("Virgo")
elif(dia>=23 and mes>=10):
    if(dia<23 and mes<=9):
        print("Libra")
elif(dia>=22 and mes>=11):
    if(dia<23 and mes<=10):
        print("Escorpio")
elif(dia>=22 and mes>=12):
    if(dia<22 and mes<=11):
        print("Saguitario")
elif(dia>=20 and mes>=1):
    if(dia<22 and mes<=12):
        print("Capricornio")
elif(dia>=19 and mes>=2):
    if(dia<20 and mes<=1):
        print("Acuario")
elif(dia>=21 and mes>=3):
    if(dia<19 and mes<=2):
        print("Pisis")
