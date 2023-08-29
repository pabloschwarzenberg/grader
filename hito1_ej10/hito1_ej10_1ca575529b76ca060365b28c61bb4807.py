saldocajero = 1000000
saldocuenta = 100000
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
if intentos != 3:
    monto = int(input('ingrese monto a retirar:'))
if monto > 100000 or monto < 0:
    print('Monto no permitido.')
else:
    print('saldo cuenta=', saldocuenta - monto)
    print('saldo cajero=',saldocajero - monto)
