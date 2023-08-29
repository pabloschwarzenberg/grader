#Zodiaco
dia = int(input("Ingrese dia de cumpleaños: "))
mes = int(input("Ingrese mes de cumpleaños: "))

if dia >=21 and mes == 3 or mes == 4 and dia < 20:
    print('ARIES')

if dia >=20 and mes == 4 or mes == 5 and dia < 21:
    print('TAURO')

if dia >=21 and mes == 5 or mes == 6 and dia < 21:
    print('GEMINIS')

if dia >=21 and mes == 6 or mes == 7 and dia < 23:
    print('CANCER')

if dia >=23 and mes == 7 or mes == 8 and dia < 23:
    print('LEO')

if dia >=23 and mes == 8 or mes == 9 and dia < 23:
    print('VIRGO')

if dia >=23 and mes == 9 or mes == 10 and dia < 23:
    print('LIBRA')

if dia >=23 and mes == 10 or mes == 11 and dia < 22:
    print('ESCORPIO')

if dia >=22 and mes == 11 or mes == 12 and dia < 22:
    print('SAGITARIO')

if dia >=22 and mes == 12 or mes == 1 and dia < 20:
    print('CAPRICORNIO')

if dia >=20 and mes == 1 or mes == 2 and dia < 19:
    print('ACUARIO')

if dia >=19 and mes == 2 or mes == 3 and dia < 20:
    print('PISCIS')      