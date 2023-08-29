#Cajero Automático
def cajero():
    saldo_cuenta = 100000
    saldo_cajero = 1000000
    intentos = 0

    while intentos < 3:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")

        if usuario == "10334151" and clave == "1803":
            print("Inicio de sesión exitoso.")
            break
        else:
            print("Usuario o clave incorrectos.")
            intentos += 1

        if intentos == 3:
            print("Tarjeta bloqueada.")
            return

    while True:
        try:
            monto = float(input("Ingrese el monto a retirar: "))
            if monto <= 0:
                print("Monto no permitido. Debe ser mayor que cero.")
            elif monto > saldo_cuenta or monto > saldo_cajero:
                print("Monto no permitido. Fondos insuficientes en la cuenta o en el cajero.")
            else:
                saldo_cuenta -= monto
                saldo_cajero -= monto
                print("Retiro exitoso.")
                print("Saldo cuenta =", saldo_cuenta)
                print("Saldo cajero =", saldo_cajero)
                break
        except ValueError:
            print("Entrada inválida. Debe ingresar un número válido.")

cajero()
