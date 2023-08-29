#saldo de cajeros 
saldo_cuenta = 100000
saldo_cajero = 1000000

intentos = 0

while True:
    usuario = input("Ingrese el número de usuario: ")
    clave = input("Ingrese la clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Inicio de sesión exitoso.")
        break
    else:
        intentos += 1
        if intentos == 3:
            print("Tarjeta bloqueada.")
            exit()
        else:
            print("Clave inválida. Por favor intente nuevamente.")

while True:
    monto = float(input("Ingrese el monto a retirar: "))

    if monto > saldo_cuenta:
        print("Monto no permitido. No cuenta con suficiente saldo.")
    else:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        print(f"Retiro exitoso. Saldo en cuenta: {saldo_cuenta}, Saldo en cajero: {saldo_cajero}")

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break

      