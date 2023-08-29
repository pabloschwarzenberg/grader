#Zodiaco
#Signo del zodiaco
##aries = 21-03 hasta <= 20-04
##tauro = 21-04 hasta <= 20-05
##geminis = 21-05 hasta <= 20-06
##cancer = 21-06 hasta <= 20-07
##leo = 21-07 hasta <= 21-08
##virgo = 22-08 hasta <= 20-09
##libra = 21-09 hasta <= 20-10
##escorpión = 21-10 hasta <= 21-11
##sagitario = 22-11 hasta <=  21-12
##capricornio = 22-12 hasta <= 20-01
##acuario = 21-01 hasta <= 19-02
##piscis = 20-02 hasta <= 20-03

dia = int(input('Ingresa tu día de nacimiento:'))
mes = int(input('Ingresa tu mes de nacimiento:'))

if (mes == 3 and dia >=21 and dia <= 31) or (mes == 4 and dia <=20 and dia >=1):
    print('aries')
if (mes == 4 and dia >=21 and dia <= 31) or (mes == 5 and dia <=20 and dia >=1):
    print('tauro')
if (mes == 5 and dia >=21 and dia <= 31) or (mes == 6 and dia <=20 and dia >=1):
    print('geminis')
if (mes == 6 and dia >=21 and dia <= 31) or (mes == 7 and dia <=20 and dia >=1):
    print('cancer')
if (mes == 7 and dia >=21 and dia <= 31) or (mes == 8 and dia <=21 and dia >=1):
    print('leo')
if (mes == 8 and dia >=22 and dia <= 31) or (mes == 9 and dia <=20 and dia >=1):
    print('virgo')
if (mes == 9 and dia >=21 and dia <= 31) or (mes == 10 and dia <=20 and dia >=1):
    print('libra')
if (mes == 10 and dia >=21 and dia <= 31) or (mes == 11 and dia <=21 and dia >=1):
    print('escorpio')
if (mes == 11 and dia >=22 and dia <= 31) or (mes == 12 and dia <=21 and dia >=1):
    print('sagitario')
if (mes == 12 and dia >=22 and dia <= 31) or (mes == 1 and dia <=20 and dia >=1):
    print('capricornio')
if (mes == 1 and dia >=21 and dia <= 31) or (mes == 2 and dia <=19 and dia >=1):
    print('acuario')
if (mes == 2 and dia >=20 and dia <= 31) or (mes == 3 and dia <=20 and dia >=1):
    print('piscis')