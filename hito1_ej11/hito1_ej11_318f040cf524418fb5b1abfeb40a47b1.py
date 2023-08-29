saldo_inicial = 1000000
saldo_usuario = 100000
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Bienvenido al cajero")
        break
    else:
        intentos_fallidos += 1
        print("Clave inválida")
        if intentos_fallidos == 3:
            print("Tarjeta bloqueada")
            exit()

while True:
    monto_retiro = int(input("Ingrese el monto a retirar: "))

    if monto_retiro > saldo_usuario:
        print("Monto no permitido")
    else:
        saldo_usuario -= monto_retiro
        saldo_inicial -= monto_retiro
        print("saldo cuenta =", saldo_usuario)
        print("saldo cajero =", saldo_inicial)
        print("billetes 20000=1")
        print("billetes 10000=3")
        print("billetes 5000=1")

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break

