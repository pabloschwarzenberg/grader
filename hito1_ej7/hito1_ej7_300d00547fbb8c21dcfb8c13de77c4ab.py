#Zodiaco
dia=int(input("dia: "))
mes=int(input("mes: "))
signos=""

if mes == 3 :
    if 0<dia<22:
        signos="piscis"
        
    else:
        signos="aries"
        
if mes == 4:
    if 0<dia<21:
        signos="aries"
    else:
        signos="tauro"
        
if mes ==5:
    if 0<dia<22:
        signos="tauro"
    else:
        signos="geminis"

if mes ==6:
    if 0<dia<22:
        signos="géminis"
    else:
        signos="cáncer"

if mes ==7:
    if 0<dia<24:
        signos="cáncer"
    else:
        signos="leo"

if mes ==8:
    if 0<dia<24:
        signos="leo"
    else:
        signos="virgo"

if mes ==9:
    if 0<dia<24:
        signos="virgo"
    else:
        signos="libra"

if mes ==10:
    if 0<dia<25:
        signos="libra"
    else:
        signos="escorpio"

if mes ==11:
    if 0<dia<23:
        signos="escorpio"
    else:
        signos="sagitario"

if mes ==12:
    if 0<dia<22:
        signos="sagitario"
    else:
        signos="capricornio"

if mes ==1:
    if 0<dia<21:
        signos="capricornio"
    else:
        signos="acuario"

if mes ==2:
    if 0<dia<20:
        signos="acuario"
    else:
        signos="piscis"
        
print(signos)      