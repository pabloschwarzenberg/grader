dia = int(input('Ingrese el día: '))
mes = int(input('Ingrese el mes: '))

if mes == 12 and dia > 22 or mes == 1 and dia <= 20:
    print('Tu signo es: Capricornio')
if mes == 1 and dia > 20 or mes == 2 and dia <= 19:
    print('Tu signo es: Acuario')
if mes == 2 and dia > 19 or mes == 3 and dia <= 21:
    print('Tu signo es: Pisis')
if mes == 3 and dia < 21 or mes == 4 and dia <= 20:
    print('Tu signo es: Aries')
if mes == 4 and dia < 20 or mes == 5 and dia <= 21:
    print('Tu signo es: Tauro')
if mes == 5 and dia < 21 or mes == 6 and dia <= 21:
    print('Tu signo es: Geminis')
if mes == 6 and dia < 21 or mes == 7 and dia <= 21:
    print('Tu signo es: Cancer')
if mes == 7 and dia < 23 or mes == 8 and dia <= 23:
    print('Tu signo es: Leo')
if mes == 8 and dia < 23 or mes == 9 and dia <= 23:
    print('Tu signo es: Virgo')
if mes == 9 and dia < 23 or mes == 10 and dia <= 23:
    print('Tu signo es: Libra')
if mes == 10 and dia < 23 or mes == 11 and dia <= 22:
    print('Tu signo es: Escorpion')
if mes == 11 and dia < 22 or mes == 12 and dia <= 22:
    print('Tu signo es: Sagitario')