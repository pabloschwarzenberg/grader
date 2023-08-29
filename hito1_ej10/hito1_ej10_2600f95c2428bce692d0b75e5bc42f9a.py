#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000

intentos = 0
bloqueado = False

while True:
    usuario = input("Ingrese el usuario: ")
    clave = input("Ingrese la clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Inicio de sesión exitoso.")
        break
    else:
        intentos += 1
        if intentos == 3:
            bloqueado = True
            print("Tarjeta bloqueada.")
            break
        else:
            print("Clave inválida. Intente nuevamente.")

while not bloqueado:
    monto = float(input("Ingrese el monto a retirar: "))

    if monto <= 0 or monto > saldo_cuenta or monto > saldo_cajero:
        print("Monto no permitido.")
    else:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        print("Retiro exitoso.")
        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)

    continuar = input("¿Desea realizar otro retiro? (S/N): ")
    if continuar.upper() != "S":
        break

