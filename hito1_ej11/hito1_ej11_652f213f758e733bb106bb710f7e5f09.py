saldo_cuenta = 100000
saldo_cajero = {
    20000: 20,
    10000: 40,
    5000: 40
}
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
            elif monto_retiro > sum(billete * cantidad for billete, cantidad in saldo_cajero.items()):
                print("El cajero no dispone de suficiente efectivo\n")
            else:
                billetes_entregados = {}
                for billete, cantidad in saldo_cajero.items():
                    billetes_entregados[billete] = min(int(monto_retiro / billete), cantidad)
                    monto_retiro -= billetes_entregados[billete] * billete
                    saldo_cajero[billete] -= billetes_entregados[billete]

                saldo_cuenta -= sum(billete * cantidad for billete, cantidad in billetes_entregados.items())
                saldo_cajero_total = sum(billete * cantidad for billete, cantidad in saldo_cajero.items())

                print("Retiro exitoso")
                print("Saldo cuenta=", saldo_cuenta,",","Saldo cajero=", saldo_cajero_total)
                for billete, cantidad in billetes_entregados.items():
                    print("Billetes", billete, "=", cantidad)
                break

        break
    else:
        intentos_fallidos += 1
        if intentos_fallidos == 3:
            print("Tarjeta bloqueada")
            break
        else:
            print("Clave inválida\n")