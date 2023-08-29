usuario = input('Usuario: ')
saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 1
respuesta = 'N'
billetes_20 = 0
billetes_10 = 0
billetes_5 = 0

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
                respuesta = input(
                    'Si desea realizar otra transaccion ingrese la letra "N", de lo contrario ingrese cualquier otra letra:  ')
                break
            else:
                saldo_cuenta -= monto
                saldo_cajero -= monto
                respuesta = input(
                    'Si desea realizar otra transaccion ingrese la letra "N", de lo contrario ingrese cualquier otra letra:  ')
                break
        else:
            print('clave invalida')
            intentos += 1
            clave = input('Clave: ')

    else:
        exit('tarjeta bloqueada')

monto_retirado = 100000 - saldo_cuenta

if monto_retirado:
    if monto_retirado // 20000 > 0:
        billetes_20 = monto_retirado // 20000
        monto_retirado -= billetes_20 * 20000
        print(monto_retirado)
    if monto_retirado // 10000 > 0:
        billetes_10 = monto_retirado // 10000
        monto_retirado -= billetes_10 * 10000
    if monto_retirado // 5000 > 0:
        billetes_5 = monto_retirado // 5000
        monto_retirado -= billetes_5 * 5000


saldo_cuenta = 'saldo cuenta=' + str(saldo_cuenta)
saldo_cajero = 'saldo cajero=' + str(saldo_cajero)


print(saldo_cuenta, saldo_cajero)

print('billetes 20000=%i' % billetes_20)
print('billetes 10000=%i' % billetes_10)
print('billetes 5000=%i' % billetes_5)