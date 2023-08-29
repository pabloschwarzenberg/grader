# Cajero Automático

# Saldo inicial en el cajero
saldo_cajero = 1000000

# Datos del usuario
usuario = "10334151"
clave = "1803"
saldo_usuario = 100000

intentos_fallidos = 0
bloqueado = False

while True:
    # Pedir usuario y clave
    input_usuario = input("Ingrese su usuario: ")
    input_clave = input("Ingrese su clave: ")

    # Validar usuario y clave
    if input_usuario == usuario and input_clave == clave:
        # Usuario y clave válidos
        while True:
            # Pedir monto a retirar
            monto_retiro = float(input("Ingrese el monto a retirar: "))

            # Validar monto a retirar
            if monto_retiro <= 0:
                print("Monto no permitido.")
            elif monto_retiro > saldo_usuario:
                print("Saldo insuficiente.")
            elif monto_retiro > saldo_cajero:
                print("El cajero no tiene suficiente saldo para realizar el retiro.")
            else:
                # Actualizar saldos
                saldo_usuario -= monto_retiro
                saldo_cajero -= monto_retiro

                # Imprimir nuevos saldos
                print(f"Saldo cuenta: {saldo_usuario}")
                print(f"Saldo cajero: {saldo_cajero}")

            opcion = input("¿Desea realizar otro retiro? (S/N): ")
            if opcion.upper() != "S":
                break
    else:
        # Usuario o clave inválidos
        intentos_fallidos += 1
        print("Clave inválida.")

        if intentos_fallidos >= 3:
            bloqueado = True
            print("Tarjeta bloqueada.")
            break

    if not bloqueado:
        opcion = input("¿Desea ingresar con otra tarjeta? (S/N): ")
        if opcion.upper() != "S":
            break
