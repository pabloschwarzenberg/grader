#Cajero Automático

usuario = int(input('Ingrese su usuario: '))

while usuario != 10334151:
    usuario = input('Error, Ingrese su usuario: ')
clave = int(input('Ingrese su clave:'))

i = 0
saldoCajero = 1000000

while not clave == 1803:
    if i < 2:
        print('clave invalida')
        clave = int(input('Ingrese su clave: '))
        i = i + 1
        if i == 3:
            print('tarjeta bloqueada')
            break
saldo1803=100000
if i !=3:
    if clave == 1803:
        monto = int(input('Monto a retirar: '))
        if monto > saldo1803 and monto < 0:
            print('monto no permitido')
            monto = int(input('Error. Monto a retirar: '))
        else:
            saldo1803 = saldo1803 - monto
            nuevoSaldoCajero = saldoCajero - monto
            print('saldo cuenta=', saldo1803)
            print('saldo cajero=', nuevoSaldoCajero)
         