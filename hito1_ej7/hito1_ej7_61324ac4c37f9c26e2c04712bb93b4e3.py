



##virgo = 23-08 hasta 23-09
##libra = 23-09 hasta 23-10
##escorpio = 23-10 hasta 22-11
##sagitario = 22-11 hasta 22-12
##capricornio = 22-12 hasta 20-01
##acuario = 20-01 hasta 19-02
##piscis = 19-02 hasta 21-03


dia = int(input('Ingresa tu día de nacimiento: '))
mes = int(input('Ingresa tu mes de nacimiento: '))

if (mes == 3  and dia >= 21) or (mes == 4 and dia <= 20):
    print ('ARIES')
elif (mes == 4 and dia >= 21) or (mes == 5 and dia <= 20):
    print ('TAURO')
elif (mes == 5  and dia >= 21) or (mes == 6 and dia <= 20):
    print ('GEMINIS')
elif (mes == 6  and dia >= 21) or (mes == 7 and dia <= 23):
    print ('CANCER')
elif (mes ==  7 and dia >= 24) or (mes == 8 and dia <= 23):
    print ('LEO')
elif (mes ==8 and dia >= 24) or (mes == 9 and dia <= 23):
    print ('VIRGO')
elif (mes ==  9 and dia >= 24) or (mes == 10 and dia <= 23):
    print ('LIBRA')
elif (mes ==  10 and dia >= 24) or (mes == 11 and dia <= 22):
    print ('ESCORPIO')
elif (mes ==  11 and dia >= 23) or (mes == 12 and dia <= 22):
    print ('SAGITARIO')
elif (mes ==  12 and dia >=23 ) or (mes == 1 and dia <= 20):
    print ('CAPRICORNIO')
elif (mes == 1  and dia >= 21) or (mes == 2 and dia <= 19):
    print ('ACUARIO')
elif (mes == 2  and dia >= 20) or (mes == 3 and dia <= 20):
    print ('PISCIS')