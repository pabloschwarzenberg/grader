#Zodiaco
dia = int(input("Ingrese su día de nacimiento: "))
mes = int(input("Ingrese su mes de nacimiento: "))
#1=enero / 2=febrero / 3=marzo / 4=abirl / 5=mayo / 6=junio
#7=julio / 8=agosto / 9=septiembre / 10=octubre / 11?nov / 12=dic
if (mes==3 and dia>=21 or mes==4 and dia<=19):
    print("Tu signo zodiacal es: Aries")
if (mes==4 and dia>=20 or mes==5 and dia<=20):
    print("Tu signo zodiacal es: Tauro")
if (mes==5 and dia>=21 or mes==6 and dia<=21):
    print("Tu signo zodiacal es: Geminis")
if (mes==6 and dia>=22 or mes==7 and dia<=22):
    print("Tu signo zodiacal es: Cancer")
if (mes==7 and dia>=23 or mes==8 and dia<=23):
    print("Tu signo zodiacal es: Leo")
if (mes==8 and dia>=24 or mes==9 and dia<=22):
    print("Tu signo zodiacal es: Virgo")
if (mes==9 and dia>=23 or mes==10 and dia<=23):
    print("Tu signo zodiacal es: Libra")
if (mes==10 and dia>=24 or mes==11 and dia<=22):
    print("Tu signo zodiacal es: Escorpio")
if (mes==11 and dia>=23 or mes==12 and dia<=22):
    print("Tu signo zodiacal es: Sagitario")
if (mes==12 and dia>=23 or mes==1 and dia<=20):
    print("Tu signo zodiacal es: Capricornio")
if (mes==1 and dia>=21 or mes==2 and dia<=18):
    print("Tu signo zodiacal es: Acuario")
if (mes==2 and dia>=19 or mes==3 and dia<=20):
    print("Tu signo zodiacal es: Piscis")
      