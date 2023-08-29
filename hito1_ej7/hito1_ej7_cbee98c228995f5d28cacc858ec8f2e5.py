#Zodiaco
d=int(input('Ingresa el día que cumples años\n'))
m=int(input('Ingresa el mes que cumples años\n'))
##Marzo - abril
if (m==3 and 21<=d<=31) or (m==4 and 1<=d<=20):
        print('Tu signo zodiacal es: Aries')
##Abril - mayo
if (m==4 and 21<=d<=30) or (m==5 and 1<=d<=20):
        print('Tu signo zodiacal es: Tauro')
##Mayo-junio
if (m==5 and 21<=d<=31) or (m==6 and 1<=d<=21):
        print('Tu signo zodiacal es: Géminis')
##Junio-julio
if (m==6 and 22<=d<=30) or (m==7 and 1<=d<=22):
        print('Tu signo zodiacal es: Cáncer')
##Julio-agosto
if (m==7 and 23<=d<=31) or (m==8 and 1<=d<=22):
        print('Tu signo zodiacal es: Leo')
##Agosto-septiembre
if (m==8 and 23<=d<=31) or (m==9 and 1<=d<=22):
        print('Tu signo zodiacal es: Virgo')
##Septiembre-octubre
if (m==9 and 23<=d<=30) or (m==10 and 1<=d<=22):
        print('Tu signo zodiacal es: Libra')
##Octubre-noviembre
if (m==10 and 23<=d<=31) or (m==11 and 1<=d<=22):
        print('Tu signo zodiacal es: Escorpio')
##Noviembre-diciembre
if (m==11 and 23<=d<=30) or (m==12 and 1<=d<=21):
        print('Tu signo zodiacal es: Sagitario')
##Diciembre-enero
if (m==12 and 22<=d<=31) or (m==1 and 1<=d<=20):
        print('Tu signo zodiacal es: Capricornio')
##Enero-Febrero
if (m==1 and 21<=d<=30) or (m==2 and 1<=d<=18):
        print('Tu signo zodiacal es: Acuario')
##Febrero-Marzo
if (m==2 and 19<=d<=29) or (m==3 and 1<=d<=20):
        print('Tu signo zodiacal es: Piscis')