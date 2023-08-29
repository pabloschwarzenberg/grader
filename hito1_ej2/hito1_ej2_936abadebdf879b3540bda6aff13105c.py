#Contestador de celular
numero = int(input('Ingrese número telefónico: '))
hora = int(input('Ingrese hora de la llamada: '))
if 0 <= hora <= 7:
    print('Resultado: CONTESTAR')
if 7 < hora < 14:
    if numero%1000 == 909:
        print('Resultado: CONTESTAR')
    else:
        print('Resultado: NO CONTESTAR')
if 14 <= hora <= 19:
    if 17 <= hora <= 19:
        if numero//100000 == 877:
            print('Resultado: NO CONTESTAR')
        else:
            print('Resultado: CONTESTAR')
    else:
        print('Resultado: NO CONTESTAR')
if hora > 19:
    print('Resultado: NO CONTESTAR')