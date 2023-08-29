#Cajero Automático
saldo_inicial_cajero = 1000000
saldo_inicial_cuenta = 100000
intentos_fallidos = 0
saldo_cuenta = saldo_inicial_cuenta
saldo_cajero = saldo_inicial_cajero

usuario_valido = 10334151
clave_valida = 1803

while True:
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario != usuario_valido or clave != clave_valida:
        intentos_fallidos += 1
        print("Clave inválida.")

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada.")
            break
    else:
        intentos_fallidos = 0
        monto = float(input("Ingrese el monto a retirar: "))

        if monto > saldo_cuenta:
            print("Monto no permitido.")
        else:
            saldo_cuenta -= monto
            saldo_cajero -= monto

            print(f"Saldo cuenta: {saldo_cuenta}")
            print(f"Saldo cajero: {saldo_cajero}")

    continuar = input("¿Desea realizar otra transacción? (S/N): ")
    if continuar.upper() == "N":
        break
    