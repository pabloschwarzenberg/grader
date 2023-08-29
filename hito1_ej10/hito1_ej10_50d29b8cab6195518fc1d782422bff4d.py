#Cajero Automático
def cajero():
    saldo_cuenta = 100000
    saldo_cajero = 1000000
    intentos = 0

    while True:
        usuario = input("Ingrese el usuario: ")
        clave = input("Ingrese la clave: ")

        if usuario == "10334151" and clave == "1803":
            intentos = 0
            print("Ingreso exitoso")
            break
        else:
            intentos += 1
            print("Clave inválida")

        if intentos == 3:
            print("Tarjeta bloqueada")
            return

    while True:
        monto = float(input("Ingrese el monto a retirar: "))

        if monto <= 0 or monto > saldo_cuenta:
            print("Monto no permitido")
        else:
            saldo_cuenta -= monto
            saldo_cajero -= monto
            print("Retiro exitoso")
            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", saldo_cajero)

        continuar = input("¿Desea realizar otra transacción? (S/N): ")
        if continuar != "S":
            break

cajero()
      