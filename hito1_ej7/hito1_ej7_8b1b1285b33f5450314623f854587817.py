dia=int(input("Ingrese día :"))
mes=int(input("Ingrese mes :"))

signo=0

if mes==3 and dia>=21:
    signo="Aries"
if mes==4 and dia<=21:
    signo="Aries"

if mes==4 and dia>=21:
    signo="Tauro"
if mes==5 and dia<=21:
    signo="Tauro"

if mes==5 and dia>=21:
    signo="Geminis"
if mes==6 and dia<=21:
    signo="Geminis"

if mes==6 and dia>=21:
    signo="Cancer"
if mes==7 and dia<=23:
    signo="Cancer"

if mes==7 and dia>=23:
    signo="Leo"
if mes==8 and dia<=23:
    signo="Leo"

if mes==8 and dia>=23:
    signo="Virgo"
if mes==9 and dia<=23:
    signo="Virgo"

if mes==9 and dia>=23:
    signo="Libra"
if mes==0 and dia<=23:
    signo="Libra"

if mes==10 and dia>=23:
    signo="Escorpion"
if mes==11 and dia<=22:
    signo="Escorpion"

if mes==11 and dia>=22:
    signo="Sagitario"
if mes==12 and dia<=22:
    signo="Sagitario"

if mes==12 and dia>=22:
    signo="Capricornio"
if mes==1 and dia<=20:
    signo="Capricornio"

if mes==1 and dia>=20:
    signo="Acuario"
if mes==2 and dia<=19:
    signo="Acuario"

if mes==2 and dia>=19:
    signo="Picis"
if mes==3 and dia<=21:
    signo="Picis"

print(signo)
