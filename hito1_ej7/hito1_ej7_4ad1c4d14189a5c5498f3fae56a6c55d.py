#Zodiaco
print('** SIGNO DEL ZODIACO **')

dia = int(input('Ingrese el día de nacimiento: '))
mes = int(input('Ingrese el mes de nacimiento(número): '))

if (dia >= 1) and (dia <= 31):
    if (mes >= 1) and (mes <= 12):
    
        if (mes == 1):
            if dia >= 21 and dia <= 31:
                print('acuario')
            elif dia >= 1 and dia <= 20:
                print('capricornio')
        elif (mes == 2):
            if dia >= 20 and dia <= 29:
                print('piscis')
            elif dia >= 1 and dia <= 19:
                print('acuario')
        elif (mes == 3):
            if dia >= 21 and dia <= 31:
                print('aries')
            elif dia >= 1 and dia <= 20:
                print('piscis')
        elif (mes == 4):
            if dia >= 21 and dia <= 30:
                print('tauro')
            elif dia >= 1 and dia <= 20:
                print('aries')
        elif (mes == 5):
            if dia >= 1 and dia <= 21:
                print('tauro')
            elif dia >= 22 and dia <= 31:
                print('geminis')
        elif (mes == 6):
            if dia >= 22 and dia <= 30:
                print('cancer')
            elif dia >= 1 and dia <= 21:
                print('geminis')
        elif (mes == 7):
            if dia >= 23 and dia <= 31:
                print('leo')
            elif dia >= 1 and dia <= 22:
                print('cancer')
        elif (mes == 8):
            if dia >= 23 and dia <= 31:
                print('virgo')
            elif dia >= 1 and dia <= 22:
                print('leo')
        elif (mes == 9):
            if dia >= 24 and dia <= 30:
                print('libra')
            elif dia >= 1 and dia <= 23:
                print('virgo')
        elif (mes == 10):
            if dia >= 24 and dia <= 31:
                print('escorpio')
            elif dia >= 1 and dia <= 23:
                print('libra')
        elif (mes == 11):
            if dia >= 23 and dia <= 30:
                print('sagitario')
            elif dia >= 1 and dia <= 22:
                print('escorpio')
        elif (mes == 12):
            if dia >= 22 and dia <= 31:
                print('capricornio')
            elif dia >= 1 and dia <= 21:
                print('sagitario')

    else:
        False
else:
    False
