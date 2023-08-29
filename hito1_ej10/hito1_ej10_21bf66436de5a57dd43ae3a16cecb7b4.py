#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

usuario_valido = 10334151
clave_valida = 1803

while True:
    usuario = int(input("Ingrese su número de usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario == usuario_valido and clave == clave_valida:
        while True:
            monto = float(input("Ingrese el monto a retirar: "))

            if monto <= 0:
                print("Monto no permitido")
            elif monto > saldo_cuenta:
                print("Saldo insuficiente")
            elif monto > saldo_cajero:
                print("El cajero no dispone de suficiente dinero")
            else:
                saldo_cuenta -= monto
                saldo_cajero -= monto
                print(f"Saldo cuenta: {saldo_cuenta}")
                print(f"Saldo cajero: {saldo_cajero}")
                break

        break
    else:
        intentos_fallidos += 1
        print("Clave inválida")

    if intentos_fallidos >= 3:
        print("Tarjeta bloqueada")
        break