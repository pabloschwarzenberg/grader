#Zodiaco
mes = int(input('Ingrese su mes de nacimiento: '))
dia = int(input('Ingrese su día de nacimiento: '))

if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20):
    print('Aries')
elif (mes == 4 and dia >= 21) or (mes == 5 and dia <= 21):
    print('Tauro')
elif (mes == 5 and dia >= 22) or (mes == 6 and dia <= 21):
    print('Geminis')
elif (mes == 6 and dia >= 22) or (mes == 7 and dia <= 22):
    print('Cancer')
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 23):
    print('Leo')
elif (mes == 8 and dia >= 24) or (mes == 9 and dia <= 23):
    print('Virgo')
elif (mes == 9 and dia >= 24) or (mes == 10 and dia <= 23):
    print('Libra')
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 22):
    print('Escorpión')
elif (mes == 11 and dia >= 23) or (mes == 12 and dia <= 22):
    print('Sagitario')
elif (mes == 12 and dia >= 23) or (mes == 1 and dia <= 20):
    print('Capricornio')
elif (mes == 1 and dia >= 21) or (mes == 2 and dia <= 18):
    print('Acuario')
elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
    print('Piscis')