#Zodiaco
dia = int(input('Ingresa el día de tu cumpleaños: '))
mes = int(input('Ingresa el mes de tu cumpleaños: '))

#ARIES: 21 Marzo – 20 Abril
if (dia >= 21 and mes == 3) or (dia < 20 and mes == 4):
    print('ARIES') 
#TAURO: 20 Abril – 21 Mayo
if (dia >= 20 and mes == 4) or (dia < 21 and mes == 5):
    print('TAURO')
#geminis: 21 mayo - 21 junio
if (dia >= 21 and mes == 5) or (dia < 21 and mes == 6):
    print('GEMINIS')
#cancer: 21 junio - 23 julio
if (dia >= 21 and mes == 6) or (dia < 23 and mes == 7):
    print('CANCER')
#leo: 23 julio - 23 agosto
if (dia >= 23 and mes == 7) or (dia < 23 and mes == 8):
    print('LEO')
#virgo: 23 agosto - 23 septiembre
if (dia >= 23 and mes == 8) or (dia < 23 and mes == 9):
    print('VIRGO')
#libra: 23 septiembre - 23 octubre
if (dia >= 23 and mes == 9) or (dia < 23 and mes == 10):
    print('LIBRA')
#escorpion: 23 octubre - 22 noviembre
if (dia >= 23 and mes == 10) or (dia < 22 and mes == 11):
    print('ESCORPION')
#sagitario: 22 noviembre - 22 diciembre
if (dia >= 22 and mes == 11) or (dia < 22 and mes == 12):
    print('SAGITARIO')
#capricornio: 22 diciembre - 20 enero
if (dia >= 22 and mes == 12) or (dia < 20 and mes == 1):
    print('CAPRICORNIO')
#acuario: 20 enero - 19 febrero 
if (dia >= 20 and mes == 1) or (dia < 19 and mes == 2):
    print('ACUARIO')
#piscis: 19 febrero - 21 marzo
if (dia >= 19 and mes == 2) or (dia < 21 and mes == 3):
    print('PISCIS')   