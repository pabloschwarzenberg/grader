#Cajero Automático
usuario = int(input('Ingrese su usuario: '))
clave = int(input('Ingrese su clave: '))
saldo_cajero = 1000000
saldo_cuanta = 100000
billetes_20 = 20
billetes_10 = 40
billetes_5 = 40

if clave != 1803:
    print('clave invalida')
    clave = int(input('Ingrese su clave: '))
    if clave != 1803:
        print('clave invalida')
        clave = int(input('Ingrese su clave: '))
        if clave != 1803:
            print('tarjeta bloqueada')
if clave == 1803:
    retiro = int(input('Ingrese el monto a retirar: '))
    if retiro > saldo_cuanta:
        print('monto no permitido')
        retiro = int(input('Ingrese el monto a retirar: '))
    if retiro <= saldo_cuanta:
        total = saldo_cuanta - retiro
        cajero = saldo_cajero - retiro
        billetes20 = retiro // 20000
        resto20 = retiro % 20000
        billetes10 = resto20 // 10000
        resto10 = resto20 % 10000
        billetes5 = resto10 // 5000
        resto5 = resto10 % 5000

        print('saldo cuenta=',total,)
        print('saldo cajero=',cajero,)
        print('billetes 20000=',billetes20,)
        print('billetes 10000=',billetes10,)
        print('billetes 5000=',billetes5,)

      