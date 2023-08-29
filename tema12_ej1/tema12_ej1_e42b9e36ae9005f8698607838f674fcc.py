def generar(n, numero='', digito=''):
    solucion = numero + digito
    if len(solucion) < n:
        soluciones = generar(n, solucion, '0') + ' '
        soluciones += generar(n, solucion, '1')
        return soluciones
    else:
        return solucion


while True:
    largo = input('Ingresa la longitud de los códigos binarios a generar: ')
    try:
        largo = int(largo)
        if largo < 1:
            raise ValueError('el número ingresado debe ser mayor a 0')
    except ValueError as error:
        print('Algo falló: {0}. Inténtalo de nuevo.'.format(error))
    else:
        break
combinaciones = generar(largo).split(' ')
for i in combinaciones:
    print(i)
