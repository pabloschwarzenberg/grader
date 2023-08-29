#Cajero Automático
saldoCajero = 1000000
billete20mil = 20
billete10mil = 40
billete5mil = 40
usuarioValido = 10334151
claveValida = 1803
saldoCuenta = 100000

usuario = int(input("Ingrese usuario: "))
while usuario != usuarioValido:
    usuario = int(input("Ingrese usuario nuevamente: "))

clave = int(input("Ingrese clave: "))
intentos = 0
while clave != claveValida:
    intentos = intentos + 1
    if intentos == 3:
        print("tarjeta bloqueada")
        break
    clave = int(input("clave invalida: "))

if intentos != 3: #continuo con el programa si la clave no esta bloqueada
    montoRetirado = int(input("Ingrese monto: "))
    if montoRetirado>saldoCajero or montoRetirado>saldoCuenta:
        print("monto no permitido")
    else:
        saldoCajero = saldoCajero - montoRetirado
        saldoCuenta = saldoCuenta - montoRetirado
        cuentaBillete20mil = 0
        cuentaBillete10mil = 0
        cuentaBillete5mil = 0
        while (montoRetirado):
            if montoRetirado >= 20000:
                cuentaBillete20mil = cuentaBillete20mil + 1
                billete20mil = billete20mil - 1
                montoRetirado = montoRetirado - 20000
            if montoRetirado >= 10000:
                cuentaBillete10mil = cuentaBillete10mil + 1
                billete10mil = billete10mil - 1
                montoRetirado = montoRetirado - 10000
            if montoRetirado >= 5000:
                cuentaBillete5mil = cuentaBillete5mil + 1
                billete5mil = billete5mil - 1
                montoRetirado = montoRetirado - 5000

        print("saldo cuenta=", saldoCuenta)
        print("saldo cajero=", saldoCajero)
        print("billetes 20000=", cuentaBillete20mil)
        print("billetes 10000=", cuentaBillete10mil)
        print("billetes 5000=", cuentaBillete5mil)