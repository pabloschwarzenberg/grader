saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 0

while True:
    usuario = input("Ingrese el usuario: ")
    clave = input("Ingrese la clave: ")

    if usuario == "10334151" and clave == "1803":
        while True:
            monto = float(input("Ingrese el monto a retirar: "))

            if monto <= 0:
                print("Monto no permitido.")
            elif monto > saldo_cuenta:
                print("Saldo insuficiente.")
            else:
                saldo_cuenta -= monto
                saldo_cajero -= monto
                print("Retiro exitoso.")
                print("Saldo cuenta = ", saldo_cuenta)
                print("Saldo cajero = ", saldo_cajero)
                break
    else:
        intentos += 1
        if intentos == 3:
            print("Tarjeta bloqueada.")
            break
        print("Clave inválida.")

    opcion = input("¿Desea realizar otra transacción? (S/N): ")
    if opcion.upper() != "S":
        break

      