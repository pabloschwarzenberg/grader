#Zodiaco
dia = int(input('Ingresa un día: '))
mes = int(input('Ingresa una mes: '))


if (dia>=21 and mes==3) or (dia<=20 and mes==4):
    print ('Su signo es Aries')
if (dia>=24 and mes==9) or (dia<=23 and mes==10):
    print ('Su signo es Libra')
if (dia>=21 and mes==4) or (dia<=21 and mes==5):
    print ('Su signo es Tauro')
if (dia>=24 and mes==10) or (dia<=22 and mes==11):
    print ('Su signo es Escorpio')
if (dia>=22 and mes==5) or (dia<=21 and mes==6):
    print ('Su signo es G\u00E9minis')
if (dia>=23 and mes==11) or (dia<=21 and mes==12):
    print ('Su signo es Sagitario')
if (dia>=21 and mes==6) or (dia<=23 and mes==7):
    print ('Su signo es C\u00E1ncer')
if (dia>=22 and mes==12) or (dia<=20 and mes==1):
    print ('Su signo es Capricornio')
if (dia>=24 and mes==7) or (dia<=23 and mes==8):
    print ('Su signo es Leo')
if (dia>=21 and mes==1) or (dia<=19 and mes==2):
    print ('Su signo es Acuario')
if (dia>=24 and mes==8) or (dia<=23 and mes==9):
    print ('Su signo es Virgo')
if (dia>=20 and mes==2) or (dia<=20 and mes==3):
    print ('Su signo es Piscis')
else:
    print('Fecha no es válida')