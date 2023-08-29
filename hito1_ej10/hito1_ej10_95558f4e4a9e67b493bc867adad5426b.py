#Cajero Automático
sc = 1000000
su = 100000
r = 0
u = ''
p = ''
i = 0
password = ''
continuar = 'N'
while continuar == 'N':
    while i < 3:
        u = int(input('ingrese su usuario'))
        p = int(input('ingrese su contraseña: '))
        if p != 1803:
            i += 1
            print('clave invalida')
            if i == 3:
                print('tarjeta bloqueada')
                break
        else:
            password = 'valida'
            break
    while su > 0 and password =='valida':
        r = int(input('ingrese el valor que desea retirar: '))
        if r > su:
            print('monto invalido')
        else:
            sc -= r
            su -= r
            print('saldo cuenta=',su)
            print('saldo cajero=',sc)
            break
    if su == 0:
            print('saldo cuenta=',su)
            break
    else:
        continuar = input('si desea continuar oprima N: ')      