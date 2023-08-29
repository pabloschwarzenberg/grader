saldo_inicial = 1000000  # Saldo inicial del cajero
saldo_usuario = 100000  # Saldo inicial del usuario
intentos = 0  # Contador de intentos fallidos de clave

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Acceso permitido")
        break
    else:
        print("Clave invalida")
        intentos += 1

    if intentos == 3:
        print("Tarjeta bloqueada")
        exit()

while True:
    monto = float(input("Ingrese el monto a retirar: "))

    if monto > saldo_usuario:
        print("Monto no permitido")
    else:
        saldo_usuario -= monto
        saldo_inicial -= monto
        print("Retiro exitoso")
        print("Saldo cuenta =", saldo_usuario)
        print("Saldo cajero =", saldo_inicial)

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion != "S" and opcion != "s":
        break
