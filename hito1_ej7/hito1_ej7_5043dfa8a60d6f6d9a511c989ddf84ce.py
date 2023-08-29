#Zodiaco
dia=int(input())
mes=int(input())
if mes==1:
    if dia>=21:
        signo="Aquario"
    elif dia<21:
        signo="Capricornio"
if mes==2:
    if dia>=20:
        signo="Piscis"
    elif dia<20:
        signo="Aquario"
if mes==3:
    if dia>=21:
        signo="Aries"
    elif dia<21:
        signo="Piscis"
if mes==4:
    if dia>=21:
        signo="Tauro"
    elif dia<21:
        signo="Aries"
if mes==5:
    if dia>=22:
        signo="Geminis"
    elif dia<=21:
        signo="Tauro"
if mes==6:
    if dia>=22:
        signo="Cancer"
    elif dia<22:
        signo="Geminis"
if mes==7:
    if dia>=23:
        signo="Leo"
    elif dia<23:
        signo="Cancer"
if mes==8:
    if dia>=23:
        signo="Virgo"
    elif dia<23:
        signo="Leo"
if mes==9:
    if dia>=23:
        signo="Libra"
    elif dia<24:
        signo="Virgo"
if mes==10:
    if dia>=24:
        signo="Escorpion"
    elif dia<24:
        signo="Libra"
if mes==11:
    if dia>=23:
        signo="Sagitario"
    elif dia<23:
        signo="Escorpion"
if mes==12:
    if dia>=22:
        signo="Capricornio"
    elif dia<22:
        signo="Sagitario"
print(signo)
     