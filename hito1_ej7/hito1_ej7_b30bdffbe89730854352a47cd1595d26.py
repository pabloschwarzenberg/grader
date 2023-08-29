#Zodiaco
dia=int(input("ingrese dia en formato dd: "))
mes=int(input("ingrese mes en formato mm: "))
signo=""
if(dia>=21 and mes==3)or(dia<=20 and mes==4):
    signo="Aries"
elif(dia>=21 and mes==4)or(dia<=20 and mes==5):
    signo="Tauro"
elif(dia>=21 and mes==5)or(dia<=21 and mes==6):
    signo="Geminis"
elif(dia>=22 and mes==6)or(dia<=22 and mes==7):
    signo="Cancer"
elif(dia>=23 and mes==7)or(dia<=22 and mes==8):
    signo="Leo"
elif(dia>=23 and mes==8)or(dia<=22 and mes==9):
    signo="Virgo"
elif(dia>=23 and mes==9)or(dia<=22 and mes==10):
    signo="Libra"
elif(dia>=23 and mes==10)or(dia<=22 and mes==11):
    signo="Escorpio"
elif(dia>=23 and mes==11)or(dia<=21 and mes==12):
    signo="Sagitario"
elif(dia>=22 and mes==12)or(dia<=20 and mes==1):
    signo="Capricornio"
elif(dia>=21 and mes==1)or(dia<=18 and mes==2):
    signo="Acuario"
elif(dia>=19 and mes==2)or(dia<=20 and mes==3):
    signo="Piscis"
print("tu signo zodiacal es :",signo)     