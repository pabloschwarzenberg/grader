saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

usuario_valido = 10334151
clave_valida = 1803

while True:
    usuario = int(input("Ingrese su número de usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario == usuario_valido and clave == clave_valida:
        print("Acceso permitido\n")

        while True:
            monto_retiro = float(input("Ingrese el monto que desea retirar: "))

            if monto_retiro <= 0:
                print("Monto no permitido\n")
            elif monto_retiro > saldo_cuenta:
                print("Saldo insuficiente\n")
            elif monto_retiro > saldo_cajero:
                print("El cajero no dispone de suficiente efectivo\n")
            else:
                saldo_cuenta -= monto_retiro
                saldo_cajero -= monto_retiro
                print("Retiro exitoso")
                print("Saldo cuenta=", round(saldo_cuenta),"Saldo cajero=", round(saldo_cajero))
                break

        break
    else:
        intentos_fallidos += 1
        if intentos_fallidos == 3:
            print("Tarjeta bloqueada")
            break
        else:
            print("Clave inválida\n")    