#Zodiaco
dia = int(input('Ingresa el número del día: '))
mes = int(input('Ingresa el número del mes: '))



if mes == '1':
    print(dia, 'de Enero ')
elif mes == '2':
    print(dia, 'de Febrero ')
elif mes == '3':
    print(dia, 'de Marzo ')
elif mes == '4':
    print(dia, 'de Abril ')        
elif mes == '5':
    print(dia, 'de Mayo ')
elif mes == '6':
    print(dia, 'de Junio ')
elif mes == '7':
    print(dia, 'de Julio ')
elif mes == '8':
    print(dia, 'de Agosto ')
elif mes == '9':
    print(dia, 'de Septiembre ')
elif mes == '10':
    print(dia, 'de Octubre ')
elif mes == '11':
    print(dia, 'de Noviembre ')
elif mes == '12':
    print(dia, 'de Diciembre ')

if (dia>=21 and mes==3) or (dia<=20 and mes==4):
    print ('Aries')
if (dia>=24 and mes==9) or (dia<=23 and mes==10):
    print ('Libra')
if (dia>=21 and mes==4) or (dia<=21 and mes==5):
    print ('Tauro')
if (dia>=24 and mes==10) or (dia<=22 and mes==11):
    print ('Escorpio')
if (dia>=22 and mes==5) or (dia<=21 and mes==6):
    print ('G\u00E9minis')
if (dia>=23 and mes==11) or (dia<=21 and mes==12):
    print ('Sagitario')
if (dia>=21 and mes==6) or (dia<=23 and mes==7):
    print ('C\u00E1ncer')
if (dia>=22 and mes==12) or (dia<=20 and mes==1):
    print ('Capricornio')
if (dia>=24 and mes==7) or (dia<=23 and mes==8):
    print ('Leo')
if (dia>=21 and mes==1) or (dia<=19 and mes==2):
    print ('Acuario')
if (dia>=24 and mes==8) or (dia<=23 and mes==9):
    print ('Virgo')
if (dia>=20 and mes==2) or (dia<=20 and mes==3):
    print ('Piscis')      