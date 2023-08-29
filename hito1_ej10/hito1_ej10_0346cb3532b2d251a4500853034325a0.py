#Cajero Automático
def cajero():
    saldo_cuenta = 100000
    saldo_cajero = 1000000
    intentos_fallidos = 0

    while True:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")

        if usuario == "10334151" and clave == "1803":
            print("¡Bienvenido!")
            saldo_cuenta = 100000
            intentos_fallidos = 0
            break
        else:
            intentos_fallidos += 1
            print("Clave inválida.")

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada.")
            return

    while True:
        monto = float(input("Ingrese el monto a retirar: "))

        if monto <= 0 or monto > saldo_cuenta:
            print("Monto no permitido.")
        else:
            saldo_cuenta -= monto
            saldo_cajero -= monto
            print("Retiro exitoso.")
            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", saldo_cajero)

        opcion = input("¿Desea realizar otro retiro? (S/N): ")

        if opcion.upper() != "S":
            break

cajero()      