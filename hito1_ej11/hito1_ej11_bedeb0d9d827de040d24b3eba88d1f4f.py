#Cajero Automático
saldoCajero = 1000000

billete20 = 20
billete10 = 40
billete5 = 40

usuarioValido = 10334151
claveValida = 1803
saldoUsuario = 100000

usuario = int(input("Ingrese usuario: "))

while usuario != usuarioValido:
    usuario = int(input("Ingrese usuario nuevamente: "))

clave = int(input("Ingrese clave: "))
intentos = 0

while clave != claveValida:
    intentos = intentos + 1

    if intentos == 3:
        print("Tarjeta bloqueada")
        break

    clave = int(input("Clave inválida: "))
if intentos != 3:
    montoRetirado = int(input("Ingrese monto: "))

if montoRetirado > saldoCajero or montoRetirado > saldoUsuario:
    print("Monto no permitido")

else:
    saldoCajero = saldoCajero - montoRetirado
    saldoUsuario = saldoUsuario - montoRetirado
    cuentaBillete20 = 0
    cuentaBillete10 = 0
    cuentaBillete5 = 0

    while montoRetirado > 0:

        if (montoRetirado >= 20000):
            cuentaBillete20 = cuentaBillete20 + 1
            billete20 = billete20 - 1
            montoRetirado = montoRetirado - 20000

        if (montoRetirado >= 10000):
            cuentaBillete10 = cuentaBillete10 + 1
            billete10 = billete10 - 1
            montoRetirado = montoRetirado - 10000

        if (montoRetirado >= 5000):
            cuentaBillete5 = cuentaBillete5 + 1
            billete5 = billete5 - 1
            montoRetirado = montoRetirado - 5000

    print("Saldo cuenta=", saldoUsuario)
    print("Saldo cajero=", saldoCajero)
    print("Billetes 20000=", cuentaBillete20)
    print("Billetes 10000=", cuentaBillete10)
    print("Billetes 5000=", cuentaBillete5)