#Zodiaco
dia = int(input("Ingrese el dia: "))
mes = int(input("Ingrese el mes: "))
signo=""


if mes==12 or mes==1:
    if mes==12 and dia>22:
       signo="capricornio"
    elif mes==1 and dia<=20:
       signo="capricornio" 

if mes==1 or mes==2:
    if mes==1 and dia>20:
        signo="acuario"
    elif mes==2 and dia<=19:
        signo="acuario"

if mes==2 or mes==3:
    if mes==2 and dia>19:
        signo="piscis"
    elif mes==3 and dia<=21:
        signo="piscis"


if mes==3 or mes==4:
    if mes==3 and dia>21:
        signo="aries"
    elif mes==4 and dia<=20:
        signo="aries"
        
if mes==4 or mes==5:
    if mes==4 and dia>20:
        signo="tauro"
    elif mes==5 and dia<=21:
        signo="tauro"

if mes==5 or mes==6:
    if mes==5 and dia>21:
        signo="geminis"
    elif mes==6 and dia<=21:
        signo="geminis"

if mes==6 or mes==7:
    if mes==6 and dia>21:
        signo="cancer"
    elif mes==7 and dia<=23:
        signo="cancer"

if mes==7 or mes==8:
    if mes==7 and dia>23:
        signo="leo"
    elif mes==8 and dia<=23:
        signo="leo"

if mes==8 or mes==9:
    if mes==2 and dia>19:
        signo="virgo"
    elif mes==3 and dia<=21:
        signo="virgo"

if mes==9 or mes==10:
    if mes==9 and dia>23:
        signo="libra"
    elif mes==10 and dia<=23:
        signo="libra"

if mes==10 or mes==11:
    if mes==10 and dia>23:
        signo="escorpion"
    elif mes==11 and dia<=22:
        signo="escorpion"

if mes==11 or mes==12:
    if mes==11 and dia>23:
        signo="sagitario"
    elif mes==12 and dia<=22:
        signo="sagitario"




print(signo)

