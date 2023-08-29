#Zodiaco
fecha=int(input('Ingrese su fecha de nacimiento en el formato MDD (Ej: 19 de Julio -> 719): '))
if 121<=fecha<=218:
    print('ACUARIO')
if 219<=fecha<=320:
    print('PISCIS')
if 321<=fecha<=420:
    print('ARIES')
if 421<=fecha<=518:
    print('TAURO')
if 521<=fecha<=621:
    print('GEMINIS')
if 622<=fecha<=722:
    print('CANCER')
if 723<=fecha<=822:
    print('LEO')
if 823<=fecha<=922:
    print('VIRGO')
if 923<=fecha<=1022:
    print('LIBRA')
if 1023<=fecha<=1122:
    print('ESCORPIO')
if 1123<=fecha<=1222:
    print('SAGITARIO')
if 1222<=fecha or fecha<120:
    print('CAPRICORNIO')