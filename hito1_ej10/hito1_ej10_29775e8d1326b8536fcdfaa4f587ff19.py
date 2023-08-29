saldo_cuenta = 100000
saldo_cajero = 1000000

intentos = 0
usuario_valido = False

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        usuario_valido = True
        break
    else:
        intentos += 1
        print("Clave inválida")

    if intentos >= 3:
        print("Tarjeta bloqueada")
        exit()

while True:
    monto = float(input("Ingrese el monto a retirar: "))

    if monto <= saldo_cuenta and monto > 0:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        print("Retiro exitoso")
        print(f"Saldo cuenta: {saldo_cuenta}")
        print(f"Saldo cajero: {saldo_cajero}")
    else:
        print("Monto no permitido")

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break

