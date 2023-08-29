#Zodiaco
dia=int(input('Ingrese su dia de cumpleanos'))
mes=input('Ingrese su mes de cumpleanos')
if mes=='3':
    if dia<21:
        print('piscis')
    elif dia>=21:
        print('aries')
elif mes == '4':
    if dia < 20:
        print('aries')
    elif dia >= 20:
        print('taurus')
elif mes == '5':
    if dia < 21:
        print('taurus')
    elif dia >=21:
        print('gemini')
elif mes == '6':
    if dia < 21:
        print('gemini')
    elif dia >= 21:
        print('cancer')
elif mes == '7':
    if dia < 23:
        print('cancer')
    elif dia >= 23:
        print('leo')
elif mes == '8':
    if dia < 23:
        print('leo')
    elif dia >= 23:
        print('virgo')
elif mes == '9':
    if dia < 23:
        print('virgo')
    elif dia >= 23:
        print('libra')
elif mes == '10':
    if dia < 23:
        print('libra')
    elif dia >= 23:
        print('escorpio')
elif mes == '11':
    if dia < 22:
        print('virgo')
    elif dia >= 23:
        print('sagitario')
elif mes == '12':
    if dia < 22:
        print('sagitario')
    elif dia >= 22:
        print('capricornio')
elif mes == '1':
    if dia < 20:
        print('capricornio')
    elif dia >= 20:
        print('aquario')
elif mes == '2':
    if dia < 19:
        print('aquario')
    elif dia >= 19:
        print('piscis')