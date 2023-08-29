#Descomponer un número
numero = (input('Ingrese un número de 4 dígitos: '))

cant_elementos = len(numero)
if cant_elementos == 4:
    print(numero[0], 'M + ',numero[1], 'C + ',numero[2], 'D + ',numero[3], 'U', sep='')
if cant_elementos == 3:
    print(numero[0], 'C + ',numero[1], 'D + ',numero[2], 'U', sep='')
if cant_elementos == 2:
    print(numero[0], 'D + ',numero[1], 'U', sep='')
if cant_elementos == 1:
    print(numero[0], 'U', sep='')
      