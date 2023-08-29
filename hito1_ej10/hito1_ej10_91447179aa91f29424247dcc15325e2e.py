saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0
usuario_valido = False

while not usuario_valido and intentos_fallidos < 3:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        usuario_valido = True
        print("Bienvenido,", usuario)
    else:
        intentos_fallidos += 1
        print("Clave inválida.")

if not usuario_valido:
    print("Tarjeta bloqueada.")
else:
    while True:
        monto_retiro = int(input("Ingrese el monto a retirar: "))

        if monto_retiro <= 0:
            print("Monto no permitido.")
            continue

        if monto_retiro > saldo_cuenta or monto_retiro > saldo_cajero:
            print("Monto no permitido.")
        else:
            saldo_cuenta -= monto_retiro
            saldo_cajero -= monto_retiro
            print("Retiro exitoso.")
            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", saldo_cajero)

        opcion = input("¿Desea realizar otro retiro? (S/N): ")
        if opcion.upper() != "S":
            break

