#Zodiaco
#===================signos zodiacales==================

signo = ['capricornio', 'acuario','piscis','aries','tauro', 'geminis', 'cancer', 'leo', 'virgo', 'libra', 'escorpio', 'sagitario']
fecha = [20,19,20,20,21,21,22,22,22,22,22,21]

#Datos al Usuario
dia = int(input('Dia de Nacimiento: '))
mes = int(input('Mes de Nacimiento: '))

mes = mes - 1
if dia > fecha[mes]:
    mes = mes + 1
if mes == 12:
    mes = 0

print('su signo zodiacal es: ',signo[mes])