#Zodiaco

dia = int(input('Ingrese día de cumpleaños: '))
mes = int(input('Ingrese día de cumpleaños: '))

if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20):
    signo = aries

signo = ('capricornio', 'acuario', 'piscis', 'aries', 'tauro', 'geminis', 'cancer', 'leo', 'virgo', 'libra', 'escorpio', 'sagitario')
fechas = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)
mes = mes - 1

if dia > fechas[mes]:
    mes = mes + 1
if mes == 12:
    mes = 0

print('Tu signo es: ', signo[mes])