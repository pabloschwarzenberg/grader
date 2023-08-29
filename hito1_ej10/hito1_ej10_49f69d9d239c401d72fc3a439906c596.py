usuario = input('Usuario: ')
saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 1
respuesta = 'N'
from sys import exit

while usuario != '10334151':
    usuario = input('Usuario: ')

clave = input('Clave: ')

while respuesta == 'N':
    while intentos < 3:

        if clave == '1803':
            monto = int(input('Monto a retirar: '))

            if monto > saldo_cuenta:
                print('monto no permitido')
                respuesta = input('Si desea realizar otra transaccion ingrese la letra "N", de lo contrario ingrese cualquier otra letra:  ')
                break
            else:
                saldo_cuenta -= monto
                saldo_cajero -= monto
                respuesta = input('Si desea realizar otra transaccion ingrese la letra "N", de lo contrario ingrese cualquier otra letra:  ')
                break
        else:
            print('clave invalida')
            intentos += 1
            clave = input('Clave: ')

    else:
        exit('tarjeta bloqueada')


saldo_cuenta = 'saldo cuenta=' + str(saldo_cuenta)
saldo_cajero = 'saldo cajero=' + str(saldo_cajero)

print(saldo_cuenta, saldo_cajero)

