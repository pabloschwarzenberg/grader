saldo_cajero = 1000000
saldo_cuanta = 100000
usuario = int(input('Ingrese su usuario:'))
while usuario != 10334151:
    usuario = int(input('Error, Ingrese usuario:'))

clave = int(input('Ingrese clave:'))
intentos = 0
while not (clave == 1803):
    intentos = intentos + 1
    if intentos == 3:
        print('Tarjeta bloqueada')
        break
    else:
        clave = int(input('Ingrese su clave:'))

if intentos != 3:
    print('seguir adelante')
monto_retirado = int(input('ingrese monto que decea retirar:'))
print('saldo cuenta=', saldo_cuanta - monto_retirado)
print('saldo cajero=', saldo_cajero - monto_retirado)