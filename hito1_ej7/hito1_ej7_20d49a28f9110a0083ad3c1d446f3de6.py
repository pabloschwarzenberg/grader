#Zodiaco
Dia = int(input('Ingresa día de tu nacimiento: '))
Mes = int(input('Ingresa mes de tu nacimiento: '))

if (Mes == 3  and Dia >= 21) or (Mes == 4 and Dia <= 20):
    print ('ARIES')
if (Mes == 4  and Dia >= 21) or (Mes == 5 and Dia <= 20):
    print ('TAURO')
if (Mes  == 5  and Dia >= 21) or (Mes  == 6 and Dia <= 20):
    print ('GEMINIS')
if (Mes  == 6  and Dia >= 21) or (Mes  == 7 and Dia <= 23):
    print ('CANCER')
if (Mes  == 7  and Dia >= 23) or (Mes  == 8 and Dia <= 23):
    print ('LEO')
if (Mes  == 8  and Dia >= 23) or (Mes  == 9 and Dia <= 23):
    print ('VIRGO')
if (Mes  == 9  and Dia >= 23) or (Mes  == 10 and Dia <= 23):
    print ('LIBRA')
if (Mes  == 10  and Dia >= 23) or (Mes  == 11 and Dia <= 22):
    print ('ESCORPIO')
if (Mes == 11 and Dia >= 22) or (Mes  == 12 and Dia <= 22):
    print ('SAGITARIO')
if (Mes  == 12 and Dia >= 22) or (Mes  == 1 and Dia <= 20):
    print ('CAPRICORNIO')
if (Mes  == 1 and Dia >= 20) or (Mes  == 2 and Dia <= 19):
    print ('ACUARIO')
if (Mes  == 2  and Dia >= 19) or (Mes  == 3 and Dia <= 21):
    print ('PISCIS')      