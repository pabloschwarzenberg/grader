#Descomponer un número
n = int(input('Ingrese un numero (de hasta 4 digitos): '))

if n > 9999:
    print('Solo de 4 digitos')
elif n < 0:
    print('Numeros positivos')
elif n > 0:
    resultado = 10000 + n
    descomposicion = str(resultado)
    mil = descomposicion[1]
    cen = descomposicion[2]
    dec = descomposicion[3]
    uni = descomposicion[4]
    print(mil + 'M + ' + cen + 'C + ' + dec + 'D + ' + uni + 'U')
