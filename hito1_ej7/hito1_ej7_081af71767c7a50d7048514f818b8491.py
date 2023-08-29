#Zodiaco
dia = int(input('Ingresa tu dia de nacimiento: '))
mes = int(input('Ingresa tu mes de nacimiento: '))

     
if (mes == 3 and 21<=dia<=31) or (mes == 4 and 1<=dia<20):
    print('ARIES')
elif (mes == 4 and 20<=dia<=30) or (mes == 5 and 1<=dia<21):
    print('TAURO')
elif (mes == 5 and 21<=dia<=31) or (mes == 6 and 1<=dia<21):
    print('GEMINIS')
elif (mes == 6 and 21<=dia<=30) or (mes == 7 and 1<=dia<23):
    print('CANCER')    
elif (mes == 7 and 23<=dia<=31) or (mes == 8 and 1<=dia<23):
    print('LEO')
elif (mes == 8 and 23<=dia<=30) or (mes == 9 and 1<=dia<23):
    print('VIRGO')
elif (mes == 9 and 23<=dia<=31) or (mes == 10 and 1<=dia<23):
    print('LIBRA')
elif (mes == 10 and 23<=dia<=30) or (mes == 11 and 1<=dia<22):
    print('ESCORPIO')
elif (mes == 11 and 22<=dia<=31) or (mes == 12 and 1<=dia<22):
    print('SAGITARIO')
elif (mes == 12 and 22<=dia<=30) or (mes == 1 and 1<=dia<20):
    print('CAPRICORNIO')
elif (mes == 1 and 20<=dia<=31) or (mes == 2 and 1<=dia<19):
    print('ACUARIO')
elif (mes == 2 and 19<=dia<=28) or (mes == 3 and 1<=dia<21):
    print('PISCIS')
 