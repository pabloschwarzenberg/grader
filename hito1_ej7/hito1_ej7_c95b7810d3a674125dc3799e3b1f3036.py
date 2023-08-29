#Zodiaco
# entrada
signo = ['capricornio', 'acuario', 'piscis', 'aries', 'tauro', 'geminis', 'cancer', 'leo' , 'virgo' , 'libra' , 'escorpio', 'sagitario']
fecha = [22, 19, 21, 20, 21, 21, 20, 23, 23, 23, 23, 22]


dia = int(input('escribe tu dia de nacimiento: '))
mes = int(input('escribe tu mes de nacimiento: '))

# procesamiento
mes = mes - 1
if dia > fecha[mes]:
    mes = mes + 1
if mes == 12:
    mes = 0

# salida
print("tu signo zodiacal es: ", signo[mes])