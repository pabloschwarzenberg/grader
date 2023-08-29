# Saldo inicial en el cajero
saldo_cajero = 1000000

# Datos del usuario autorizado
usuario_autorizado = "10334151"
clave_autorizada = "1803"
saldo_usuario = 100000

# Contador de intentos fallidos
intentos_fallidos = 0

# Bucle principal del programa
while True:
    # Solicitar usuario y clave
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    # Verificar si la clave es válida
    if usuario == usuario_autorizado and clave == clave_autorizada:
        # Reiniciar contador de intentos fallidos
        intentos_fallidos = 0

        # Solicitar monto a retirar
        monto = float(input("Ingrese el monto a retirar: "))

        # Verificar si el monto es válido
        if monto > saldo_usuario:
            print("Monto no permitido")
        else:
            # Actualizar saldos
            saldo_usuario -= monto
            saldo_cajero -= monto

            # Imprimir saldos actualizados
            print("Saldo cuenta =", saldo_usuario)
            print("Saldo cajero =", saldo_cajero)
    else:
        print("Clave inválida")
        intentos_fallidos += 1

        # Verificar si se superó el límite de intentos fallidos
        if intentos_fallidos >= 3:
            print("Tarjeta bloqueada")
            break

    # Preguntar si se desea continuar
    opcion = input("¿Desea realizar otra transacción? (S/N): ")
    if opcion.upper() != "S":
        break
