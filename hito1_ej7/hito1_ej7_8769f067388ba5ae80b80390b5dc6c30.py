#Zodiaco
Dia = int(input("Ingrese su dia de cumpleaños: "))
Mes = int(input("Ingrese su mes de cumpleaños: "))

Signos = ["Aries","Tauro","Geminis","Cancer","Leo","Virgo","Libra","Escorpio","Sagitario","Capricornio","Acuario","Piscis"]

if(Dia>=21 and Mes==3) or (1<=Dia<20 and Mes==4):
    Signo = Signos[0]

if(Dia>=20 and Mes==4) or (1<=Dia<21 and Mes==5):
    Signo = Signos[1]

if(Dia>=21 and Mes==5) or (1<=Dia<21 and Mes==6):
    Signo = Signos[2]

if(Dia>=21 and Mes==6) or (1<=Dia<23 and Mes==7):
    Signo = Signos[3]

if(Dia>=23 and Mes==7) or (1<=Dia<23 and Mes==8):
    Signo = Signos[4]

if(Dia>=23 and Mes==8) or (1<=Dia<23 and Mes==9):
    Signo = Signos[5]

if(Dia>=23 and Mes==9) or (1<=Dia<23 and Mes==10):
    Signo = Signos[6]

if(Dia>=23 and Mes==10) or (1<=Dia<22 and Mes==11):
    Signo = Signos[7]

if(Dia>=22 and Mes==11) or (1<=Dia<22 and Mes==12):
    Signo = Signos[8]

if(Dia>=22 and Mes==12) or (1<=Dia<20 and Mes==1):
    Signo = Signos[9]

if(Dia>=22 and Mes==1) or (1<=Dia<19 and Mes==2):
    Signo = Signos[10]

if(Dia>=19 and Mes==2) or (1<=Dia<21 and Mes==3):
    Signo = Signos[11]

print("Su signo zodiacal es: ",Signo)