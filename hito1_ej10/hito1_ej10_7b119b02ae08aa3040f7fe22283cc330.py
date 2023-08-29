#Cajero Automático
saldo_inicial = 1000000
saldo_usuario = 100000
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Bienvenido/a")
        break
    else:
        print("Usuario o clave incorrectos")
        intentos_fallidos += 1

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada")
            exit()

while True:
    monto_retiro = float(input("Ingrese el monto a retirar: "))

    if monto_retiro > saldo_usuario:
        print("Monto no permitido")
    else:
        saldo_usuario -= monto_retiro
        saldo_inicial -= monto_retiro
        print("Retiro exitoso")
        print("Saldo cuenta =", saldo_usuario)
        print("Saldo cajero =", saldo_inicial)

    opcion = input("¿Desea realizar otro retiro? (S/N): ")

    if opcion != "S":
        break

