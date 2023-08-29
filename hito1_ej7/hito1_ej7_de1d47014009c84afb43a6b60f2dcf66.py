#Zodiaco
d = eval(input('Ingrese su día de nacimiento: '))
m = eval(input('Ingrese su mes de nacimiento: '))


if (m == 3  and d >= 21) or (m == 4 and d <= 20):
    print ('ARIES')
if (m == 4  and d >= 21) or (m == 5 and d <= 20):
    print ('TAURO')
if (m == 5  and d >= 21) or (m == 6 and d <= 20):
    print ('GEMINIS')
if (m == 6  and d >= 21) or (m == 7 and d <= 23):
    print ('CANCER')
if (m == 7  and d >= 23) or (m == 8 and d <= 23):
    print ('LEO')
if (m == 8  and d >= 23) or (m == 9 and d <= 23):
    print ('VIRGO')
if (m == 9  and d >= 23) or (m == 10 and d <= 23):
    print ('LIBRA')
if (m == 10  and d >= 23) or (m == 11 and d <= 22):
    print ('ESCORPIO')
if (m == 11  and d >= 22) or (m == 12 and d <= 22):
    print ('SAGITARIO')
if (m == 12  and d >= 22) or (m == 1 and d <= 20):
    print ('CAPRICORNIO')
if (m == 1  and d >= 20) or (m == 2 and d <= 19):
    print ('ACUARIO')
if (m == 2  and d >= 19) or (m == 3 and d <= 21):
    print ('PISCIS')


      