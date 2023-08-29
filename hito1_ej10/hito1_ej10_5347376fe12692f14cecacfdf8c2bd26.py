#Cajero Automático

saldoCajero = 1000000
usuarioValido = 10334151
claveValida = 1803
saldoCuenta = 100000

usuario = int(input('Ingrese usuario: '))

while usuario != usuarioValido:
    usuario = int(input('Ingrese usuario nuevamente: '))

clave = int(input('Ingrese clave: '))

intentos = 0

while clave != claveValida:
    intentos = intentos + 1
    if intentos == 3:
        print('Tarjeta bloqueada')
        break
    clave = int(input('Clave invalida: '))

    
if intentos != 3:
    montoRetirado = int(input('Ingrese monto: '))
    if montoRetirado >= saldoCajero or montoRetirado > saldoCuenta:
        print('Monto no permitido')
    else:
        saldoCajero = saldoCajero - montoRetirado
        saldoCuenta = saldoCuenta - montoRetirado
        print('Saldo cuenta=',saldoCuenta)
        print('Saldo cajero=',saldoCajero)