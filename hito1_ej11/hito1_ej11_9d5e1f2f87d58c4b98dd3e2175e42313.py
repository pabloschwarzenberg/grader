# Cajero Automático Nivel 2

# Saldo inicial en el cajero
saldo_cajero = {
    20000: 20,
    10000: 40,
    5000: 40
}

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
            elif monto_retiro > sum(saldo_cajero.keys()):
                print("El cajero no tiene suficiente saldo para realizar el retiro.")
            else:
                # Distribuir el monto en los billetes disponibles
                billetes_entregados = {}

                for denominacion, cantidad_disponible in saldo_cajero.items():
                    cantidad_entregada = min(int(monto_retiro / denominacion), cantidad_disponible)
                    billetes_entregados[denominacion] = cantidad_entregada
                    monto_retiro -= cantidad_entregada * denominacion
                    saldo_cajero[denominacion] -= cantidad_entregada

                # Imprimir billetes entregados
                for denominacion, cantidad_entregada in billetes_entregados.items():
                    print(f"billetes {denominacion}={cantidad_entregada}")

                # Actualizar saldo del usuario
                saldo_usuario -= sum(billetes_entregados.values())

                # Imprimir nuevos saldos
                print(f"Saldo cuenta: {saldo_usuario}")
                print("Saldo cajero:")
                for denominacion, cantidad_disponible in saldo_cajero.items():
                    print(f"billetes {denominacion}={cantidad_disponible}")

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
