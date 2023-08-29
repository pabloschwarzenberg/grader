#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Ingreso exitoso.")
        break
    else:
        intentos += 1
        print("Clave inválida.")
        if intentos == 3:
            print("Tarjeta bloqueada.")
            exit()

while True:
    try:
        monto = int(input("Ingrese el monto a retirar: "))
        if monto > saldo_cuenta:
            print("Monto no permitido. Saldo insuficiente en la cuenta.")
        elif monto > saldo_cajero:
            print("Monto no permitido. Saldo insuficiente en el cajero.")
        else:
            saldo_cuenta -= monto
            saldo_cajero -= monto

            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", saldo_cajero)
    except ValueError:
        print("Error: El monto ingresado no es válido. Por favor, ingrese un número válido.")

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break
  