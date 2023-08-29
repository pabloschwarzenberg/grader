saldo_cajero = 1000000
usuario = 10334151
clave = 1803
saldo_cuenta = 100000
billetes_20 = 20
billetes_10 = 40
billetes_5 = 40

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
        copia = monto_a_retirar
        if billetes_20 > 0:
            billetes_20_mensaje = copia // 20000
            billetes_20 -= billetes_20_mensaje
            copia -= (20000 * billetes_20_mensaje)
            print("billetes 20000=",billetes_20_mensaje)
        if billetes_10 > 0:
            billetes_10_mensaje = copia // 10000
            billetes_10 -= billetes_10_mensaje
            copia -= (10000 * billetes_10_mensaje)
            print("billetes 10000=",billetes_10_mensaje)
        if billetes_5 > 0:
            billetes_5_mensaje = copia // 5000
            billetes_5 -= billetes_5_mensaje
            copia -= (5000 * billetes_5_mensaje)
            print("billetes 5000=",billetes_5_mensaje)

        saldo_cajero -=  monto_a_retirar
        saldo_cuenta -=  monto_a_retirar
        print("saldo cuenta=", saldo_cuenta)
        print("saldo cajero=", saldo_cajero)
