#Zodiaco
dia=int(input("Ingresar día de nacimiento: "))
mes=int(input("Ingresar mes de nacimiento: "))

signo_zodiacal=""

if ((dia>=21 and dia<=31) and mes==3) or ((dia>=1 and dia<=20) and mes==4):
    signo_zodiacal="Aries"
    #print(signo_zodiacal)
if ((dia>20 and dia<=30) and mes==4) or ((dia>=1 and dia<=21) and mes==5):
    signo_zodiacal="Tauro" 
if ((dia>21 and dia<=31) and mes==5) or ((dia>=1 and dia<=21) and mes==6):
    signo_zodiacal="Geminis"
if ((dia>21 and dia<=30) and mes==6) or ((dia>=1 and dia<=23) and mes==7):
    signo_zodiacal="Cancer"
if ((dia>23 and dia<=31) and mes==7) or ((dia>=1 and dia<=23) and mes==8):
    signo_zodiacal="Leo"
if ((dia>23 and dia<=31) and mes==8) or ((dia>=1 and dia<=23) and mes==9):
    signo_zodiacal="Virgo"
if ((dia>23 and dia<=30) and mes==9) or ((dia>=1 and dia<=23) and mes==10):
    signo_zodiacal="Libra"
if ((dia>23 and dia<=31) and mes==10) or ((dia>=1 and dia<=22) and mes==11):
    signo_zodiacal="Ecorpio"
if ((dia>=23 and dia<=30) and mes==11) or ((dia>=1 and dia<=22) and mes==12):
    signo_zodiacal="Sagitario"
if ((dia>22 and dia<=31) and mes==12) or ((dia>=1 and dia<=20) and mes==1):
    signo_zodiacal="Capricornio"
if ((dia>20 and dia<=31) and mes==1) or ((dia>=1 and dia<=19) and mes==2):
    signo_zodiacal="acuario"
if ((dia>19 and dia<=29) and mes==2) or ((dia>=1 and dia<=20) and mes==3):
    signo_zodiacal="piscis"

print(signo_zodiacal)