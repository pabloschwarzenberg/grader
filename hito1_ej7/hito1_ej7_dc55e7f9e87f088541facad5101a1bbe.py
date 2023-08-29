dia=int(input("Ingrese dia de cumpleaños: "))
mes=int(input("Ingrese mes de cumpleaños (como numero): "))
if (dia>=21 and mes==3) or (dia<20 and mes==4):
    sz="Aries"
if (dia>=20 and mes==4) or (dia<21 and mes==5):
    sz="Tauro"
if (dia>=21 and mes==5) or (dia<21 and mes==6):
    sz="Geminis"
if (dia>=21 and mes==6) or (dia<23 and mes==7):
    sz="Cancer"
if (dia>=23 and mes==7) or (dia<23 and mes==8):
    sz="Leo"
if (dia>=23 and mes==8) or (dia<23 and mes==9):
    sz="Virgo"
if (dia>=23 and mes==9) or (dia<23 and mes==10):
    sz="Libra"
if (dia>=23 and mes==10) or (dia<22 and mes==11):
    sz="Escorpio"
if (dia>=22 and mes==11) or (dia<22 and mes==12):
    sz="Sagitario"
if (dia>=22 and mes==12) or (dia<20 and mes==1):
    sz="Capricornio"
if (dia>=20 and mes==1) or (dia<19 and mes==2):
    sz="Acuario"
if (dia>=19 and mes==2) or (dia<21 and mes==3):
    sz="Piscis"
print (sz)
