saldo_cajero = 1000000
usuario = 10334151
clave = 1803
saldo_cuenta = 100000

usuario_entrada = int(input("Ingrese su usuario de cajero: "))
while usuario_entrada != usuario:
    usuario_entrada = int(input("Ingrese nuevamente su usuario de cajero: "))

intentos_clave = 0
clave_entrada = int(input("Ingrese su clave de cajero : "))
while clave_entrada != clave:
    intentos_clave += 1
    if intentos_clave == 3:
        print("Tarjeta bloqueada")
        break
    clave_entrada =  int(input("Ingrese nuevamente su clave de cajero : "))

if intentos_clave != 3:
    monto_a_retirar = int(input("Ingrese el monto a retirar: "))

    if monto_a_retirar>saldo_cajero or monto_a_retirar>saldo_cuenta:
        print("monto no permitido")

    else:
        saldo_cajero -=  monto_a_retirar
        saldo_cuenta -=  monto_a_retirar
        print("saldo cuenta=", saldo_cuenta)
        print("saldo cajero=", saldo_cajero)