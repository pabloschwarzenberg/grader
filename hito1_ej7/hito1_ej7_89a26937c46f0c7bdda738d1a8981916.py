#Zodiaco
a = int (input ('Ingrese su día de nacimiento: '))
mes = int (input ('Ingrese su mes (número del mes) de nacimiento: '))
if (a>=21 and mes==3) or (a<=20 and mes==4):
    print ('Tu signo es: Aries')
if (a >= 21 and mes == 4) or (a <= 21 and mes == 5):
    print('Tu signo es: Tauro')
if (dia >= 22 and mes == 5) or (a <= 21 and mes == 6):
    print('Tu signo es: Geminis')
if (dia>=21 and mes==6) or (dia<=23 and mes==7):
    print ('Tu signo es: Cancer')
if (dia >= 24 and mes == 7) or (dia <= 23 and mes == 8):
    print('Tu signo es: Leo')
if (dia >= 24 and mes == 8) or (dia <= 23 and mes == 9):
    print('Tu signo es: Virgo')
if (dia>=24 and mes==9) or (dia<=23 and mes==10):
    print ('Tu signo es: Libra')
if (dia>=24 and mes==10) or (dia<=22 and mes==11):
    print ('Tu signo es: Escorpio')
if (dia>=23 and mes==11) or (dia<=21 and mes==12):
    print ('Tu signo es: Sagitario')
if (dia>=22 and mes==12) or (dia<=20 and mes==1):
    print ('Tu signo es: Capricornio')
if (dia>=21 and mes==1) or (dia<=19 and mes==2):
    print ('Tu signo es: Acuario')
if (dia>=20 and mes==2) or (dia<=20 and mes==3):
    print ('Tu signo es: Piscis')