numero = eval(input('Ingrese numero telefonico:'''  ))
hora = eval(input('Ingrese hora llamada:'''  ))
if (0 <= hora <= 7):
    print('CONTESTAR')
if 17 <= hora:
    print('NO CONTESTAR')
ultimos = numero % 1000
primeros = numero // 100000
if (17 <= hora <= 19) and (primeros == 877):
    print('CONTESTAR')
if (7 < hora < 14):
    if ultimos == 909:
        print('CONTESTAR')
    else:
        print('NO CONTESTAR')