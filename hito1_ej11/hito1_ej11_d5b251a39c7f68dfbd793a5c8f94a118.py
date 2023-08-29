#Cajero Automático
saldo_inicial = 1000000
saldo_usuario = 100000
intentos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Inicio de sesión exitoso.")
        break
    else:
        intentos += 1
        print("Clave inválida.")

    if intentos >= 3:
        print("Tarjeta bloqueada.")
        exit()

while True:
    monto_retiro = float(input("Ingrese el monto a retirar: "))

    if monto_retiro > saldo_inicial:
        print("Monto no permitido. Saldo insuficiente.")
    else:
        saldo_inicial -= monto_retiro
        saldo_usuario -= monto_retiro
        print("Retiro exitoso.")
        print("saldo cajero: ", saldo_inicial)
        print("saldo cuenta: ", saldo_usuario)

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break