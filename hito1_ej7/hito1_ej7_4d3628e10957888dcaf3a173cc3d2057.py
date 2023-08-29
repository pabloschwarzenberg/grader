#Zodiaco
dia = int(input('Ingresa el dia de tu cumpleaños: '))
mes = int(input('Ingresa el numero del mes de tu cumpleaños: '))

if dia >= 21 and mes == 3 or 1 <= dia < 20 and mes == 4:
    print('Signo Aries')
if dia >= 20 and mes == 4 or 1 <= dia < 21 and mes == 5:
    print('Signo Tauro')
if dia >= 21 and mes == 5 or 1 <= dia < 21 and mes == 6:
    print('Signo Geminis')
if 1 <= dia <= 31 and 6 <= mes <= 7:
    print('Signo Cancer')
if 1 <= dia <= 31 and 7 <= mes <= 8:
    print('Signo Leo')
if 1 <= dia <= 31 and 8 <= mes <= 9:
    print('Signo Virgo')
if 1 <= dia <= 31 and 9 <= mes <= 10:
    print('Signo Libra')
if 1 <= dia <= 31 and 10 <= mes <= 11:
    print('Signo Escorpio')
if 1 <= dia <= 31 and 11 <= mes <= 12:
    print('Signo Sagitario')
if 1 <= dia <= 31 and 12 <= mes <= 1:
    print('Signo Capricornio')
if 1 <= dia <= 31 and 1 <= mes <= 2:
    print('Signo Acuario')
if 1 <= dia <= 31 and 2 <= mes <= 3:
    print('Signo Piscis')
    