dia = int(input('Ingresa tu día de nacimiento: '))
mes = int(input('Ingresa tu mes de nacimiento: '))

## Abajo: if 21-03 <= fechaNacimiento <= 20-04:

if (mes == 3  and dia >= 21) or (mes == 4 and dia <= 20):
    print ('ARIES')
if (mes == 2 and dia >= 19) or (mes == 3 and dia <= 21):
    print ('Piscis')
if (mes == 5 and dia >= 21) or (mes == 6 and dia <= 21):
    print ('Gemini')
if (mes == 6 and dia >= 21) or (mes == 7 and dia <= 23):
    print ('Cancer')
if (mes == 7 and dia >= 23) or (mes == 8 and dia <= 23):
    print ('Leo')
if (mes == 8 and dia >= 23) or (mes == 9 and dia <= 23):
    print ('Virgo')
if (mes == 9 and dia >= 23) or (mes == 10 and dia <= 23):
    print('Libra')
if (mes == 10 and dia >= 23) or (mes == 11 and dia <= 22):
    print('Escorpio')
if (mes == 11 and dia >= 22) or (mes == 12 and dia <= 22):
    print('Sagitario')
if (mes == 12 and dia >= 22) or (mes == 1 and dia <= 20):
    print('Capricornio')
if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 19):
    print('Acuario')
if (mes == 4 and dia >= 20) or (mes == 5 and dia <= 21):
    print ('Tauro')