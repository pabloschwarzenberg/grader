saldocajero = 1000000
saldocuenta = 100000
b20 = 20
b10 = 40
b5 = 40
usuario = int(input('Ingrese su usuario:'))
while usuario != 10334151:
    usuario = int(input('ERROR, Ingrese usuario:'))
clave = int(input('Ingrese su clave:'))
intentos = 0
while not (clave == 1803):
    intentos = intentos + 1
    print('intentos:', intentos)
    if intentos == 3:
        print('Targeta bloqueada.')
        break
    else:
        clave = int(input('ingrese su clave:'))
if intentos < 3:
    monto = int(input('ingrese monto a retirar:'))
    print('saldo cuenta=', saldocuenta - monto)
    print('saldo cajero=', saldocajero - monto)
    retira20 = 0
    retira10 = 0
    retira5 = 0
    while monto > 0:
        if monto >= 20000 and b20 > 0:
            retira20 = retira20 + 1
            b20 = b20 - 1
            monto = monto - 20000
        if monto >= 10000 and b10 > 0:
            retira10 = retira10 + 1
            b10 = b10 - 1
            monto = monto - 10000
        if monto >= 5000 and b5 > 0:
            retira5 = retira5 + 1
            b5 = b5 - 1
            monto = monto - 5000

if monto > 100000 or monto < 0:
    print('Monto no permitido.')
else:
    print('billetes 20000=', retira20)
    print('billetes 10000=', retira10)
    print('billetes 5000=', retira5)

      