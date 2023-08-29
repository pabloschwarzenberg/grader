saldo_inicial = 1000000
saldo_cajero = 1000000
intentos_fallidos = 0

usuario_valido = 10334151
clave_valida = 1803
saldo_usuario = 100000

while True:
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario == usuario_valido and clave == clave_valida:
        print("Bienvenido al cajero automático")
        break
    else:
        print("Usuario o clave incorrectos")
        intentos_fallidos += 1

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada")
        exit()

while True:
    try:
        monto_retiro = int(input("Ingrese el monto a retirar: "))
    except ValueError:
        print("Error: Ingrese un valor numérico válido.")
        continue

    if monto_retiro <= saldo_usuario:
        if monto_retiro <= saldo_cajero:
            saldo_usuario -= monto_retiro
            saldo_cajero -= monto_retiro
            print("Retiro exitoso")
            print("saldo cuenta=" + str(saldo_usuario))
            print("saldo cajero=" + str(saldo_cajero))
        else:
            print("Monto no permitido: Fondos insuficientes en el cajero")
    else:
        print("Monto no permitido: Fondos insuficientes en la cuenta")

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break
