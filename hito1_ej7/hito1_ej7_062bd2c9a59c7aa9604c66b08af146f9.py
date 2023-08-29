#Zodiaco
#HITO 1 - EJERCICIO 8: Signo del Zodíaco

# Escribe un programa que reciba como parámetro el día y el mes del
# cumpleaños de una persona (como números enteros) y que imprima el
# signo del zodíaco al que pertenece.
# Para determinar las fechas de cada signo utiliza la columna
# Tropical Zodiac en la tabla de fechas que aparece en este link:

# LINK: en.wikipedia.org/wiki/Zodiac#Table_of_dates

##aries = 21-03 hasta <= 20-04
##tauro = 21-04 hasta <= 20-05
##geminis = 21-05 hasta <= 20-06

##cancer = 21-06 hasta 23-07
##leo = 23-07 hasta 23-08
##virgo = 23-08 hasta 23-09
##libra = 23-09 hasta 23-10
##escorpio = 23-10 hasta 22-11
##sagitario = 22-11 hasta 22-12
##capricornio = 22-12 hasta 20-01
##acuario = 20-01 hasta 19-02
##piscis = 19-02 hasta 21-03

dia = int(input('Ingresa tu día de nacimiento: '))
mes = int(input('Ingresa tu mes de nacimiento: '))

## Abajo: if 21-03 <= fechaNacimiento <= 20-04:

if (mes == 3  and dia >= 21) or (mes == 4 and dia <= 20):
    print ('ARIES')
if (mes == 4  and dia >= 21) or (mes == 5 and dia <= 20):
    print ('TAURO')
if (mes == 5  and dia >= 21) or (mes == 6 and dia <= 20):
    print ('GEMINIS')
if (mes == 6  and dia >= 21) or (mes == 7 and dia <= 23):
    print ('CANCER')
if (mes == 7  and dia >= 23) or (mes == 8 and dia <= 23):
    print ('LEO')
if (mes == 8  and dia >= 23) or (mes == 9 and dia <= 23):
    print ('VIRGO')
if (mes == 9  and dia >= 23) or (mes == 10 and dia <= 23):
    print ('LIBRA')
if (mes == 10  and dia >= 23) or (mes == 11 and dia <= 22):
    print ('ESCORPIO')
if (mes == 11 and dia >= 22) or (mes == 12 and dia <= 22):
    print ('SAGITARIO')
if (mes == 12 and dia >= 22) or (mes == 1 and dia <= 20):
    print ('CAPRICORNIO')
if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 19):
    print ('ACUARIO')
if (mes == 2  and dia >= 19) or (mes == 3 and dia <= 21):
    print ('PISCIS')

      