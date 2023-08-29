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
    contadorBillete20 = 0
    contadorBillete10 = 0
    contadorBillete5 = 0

    while montoRetirado > 0:

        if (montoRetirado >= 20000):
            contadorBillete20 = contadorBillete20 + 1
            billete20 = billete20 - 1
            montoRetirado = montoRetirado - 20000

        if (montoRetirado >= 10000):
            contadorBillete10 = contadorBillete10 + 1
            billete10 = billete10 - 1
            montoRetirado = montoRetirado - 10000

        if (montoRetirado >= 5000):
            contadorBillete5 = contadorBillete5 + 1
            billete5 = billete5 - 1
            montoRetirado = montoRetirado - 5000

    print("Saldo cuenta=", saldoUsuario)
    print("Saldo cajero=", saldoCajero)
    print("Billetes 20000=", contadorBillete20)
    print("Billetes 10000=", contadorBillete10)
    print("Billetes 5000=", contadorBillete5)