#Signos Zodiacales
dia = int(input('Ingresa el día de tu cumpleaños: '))
mes = int(input('Ingresa el mes de tu cumpleaños: '))

signo = ''
#Validación de los datos ingresados
if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        signo = 'Acuario'
elif (mes == 2 and dia >= 19) or (mes == 3 and dia <=20):
        signo = 'Piscis'
elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        signo = 'Aries'
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        signo = 'Tauro'
elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        signo = 'Geminis'
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        signo = 'Cancer'
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        signo = 'Leo'
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        signo = 'Libra'
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 21):
        signo ='Escorpio'
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        signo = 'Sagitario'
else: 
        signo = 'Capricornio'

print("Tu signo Zodiacal es", signo)
