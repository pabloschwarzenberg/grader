#Zodiaco
dia = int(input('Ingrese el dia que nacio: '))
mes = int(input('Ingrese el mes que nacio como numero: '))

if (mes == 3 and dia >= 21 or mes == 4 and dia <= 19):
    print('Su signo es Aries')
elif (mes == 4 and dia >= 20 or mes == 5 and dia <= 20):
    print('Su signo es tauro')
elif (mes == 5 and dia >= 21 or mes == 6 and dia <= 20):
    print('Su signo es geminis')
elif (mes == 6 and dia >= 21 or mes == 7 and dia <= 22):
    print('Su signo es cancer')
elif (mes == 7 and dia >= 23 or mes == 8 and dia <= 22):
    print('Su signo es leo')
elif (mes == 8 and dia >= 23 or mes == 9 and dia <= 22):
    print('Su signo es virgo')
elif (mes == 9 and dia >= 23 or mes == 10 and dia <= 22):
    print('Su signo es libra')
elif (mes == 10 and dia >= 23 or mes == 11 and dia <= 21):
    print('Su signo es escorpio')
elif (mes == 11 and dia >= 22 or mes == 12 and dia <= 21):
    print('Su signo es sagitario')
elif (mes == 12 and dia >= 22 or mes == 1 and dia <= 19):
    print('Su signo es capricornio')
elif (mes == 1 and dia >= 20 or mes == 2 and dia <= 18):
    print('Su signo es acuario')
elif (mes == 2 and dia >= 19 or mes == 3 and dia <= 20):
    print('Su signo es piscis')  