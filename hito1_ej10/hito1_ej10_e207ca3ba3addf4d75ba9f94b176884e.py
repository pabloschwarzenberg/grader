# Saldo inicial del cajero
saldo_cajero = 1000000

# Datos del usuario
usuario_valido = "10334151"
clave_valida = "1803"
saldo_usuario = 100000

# Contadores de intentos fallidos y bloqueo
intentos_fallidos = 0
bloqueado = False

# Bucle principal del programa
while True:
    # Solicitar usuario y clave
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    # Verificar clave y bloqueo
    if usuario == usuario_valido and clave == clave_valida:
        if bloqueado:
            print("Tarjeta bloqueada. Contacte al banco.")
            break
        else:
            # Solicitar monto a retirar
            monto = float(input("Monto a retirar: "))

            # Verificar monto permitido
            if monto <= saldo_usuario:
                # Actualizar saldos
                saldo_usuario -= monto
                saldo_cajero -= monto

                # Imprimir saldos actualizados
                print("Saldo cuenta: ", saldo_usuario)
                print("Saldo cajero: ", saldo_cajero)
            else:
                print("Monto no permitido.")
    else:
        print("Clave inválida.")
        intentos_fallidos += 1

        # Verificar intentos fallidos
        if intentos_fallidos == 3:
            print("Tarjeta bloqueada. Contacte al banco.")
            bloqueado = True

    # Preguntar si se desea salir del programa
    opcion = input("¿Desea realizar otra transacción? (S/N): ")
    if opcion != "S":
        break
