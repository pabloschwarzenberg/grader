numero = input('Ingrese un número de hasta 4 dígitos: ')

if len(numero) > 4:
    print('El número ingresado tiene más de 4 dígitos')
    exit()

numero = numero.zfill(4)

miles = int(numero[0])
centenas = int(numero[1])
decenas = int(numero[2])
unidades = int(numero[3])

descomposicion = ''
if miles > 0:
    descomposicion = descomposicion + str(miles) + 'M + '
if centenas > 0:
    descomposicion = descomposicion + str(centenas) + 'C + '
if decenas > 0:
    descomposicion = descomposicion + str(decenas) + 'D + '
descomposicion = descomposicion + str(unidades) + 'U'

print('Descomposición:', descomposicion)
