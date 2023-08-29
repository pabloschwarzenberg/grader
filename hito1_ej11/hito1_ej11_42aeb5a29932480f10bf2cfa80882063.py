#Cajero Automático
# Saldo inicial del cajero y del usuario
saldo_cajero = {
    20000: 20,
    10000: 40,
    5000: 40
}

saldo_usuario = 100000

# Número máximo de intentos de clave
intentos_maximos = 3
intentos = 0

# Datos del usuario autorizado
usuario_autorizado = {
    "usuario": "10334151",
    "clave": "1803"
}

# Bucle principal del programa
while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    # Verificar si el usuario y la clave son válidos
    if usuario == usuario_autorizado["usuario"] and clave == usuario_autorizado["clave"]:
        print("Ingreso exitoso.")

        # Bucle para gestionar las transacciones del usuario
        while True:
            monto_retiro = int(input("Ingrese el monto a retirar: "))

            # Verificar si el monto a retirar es válido
            if monto_retiro <= 0 or monto_retiro % 5000 != 0:
                print("Monto no permitido.")
            elif monto_retiro > saldo_usuario:
                print("Saldo insuficiente.")
            else:
                # Realizar el retiro
                saldo_usuario -= monto_retiro

                # Actualizar los billetes del cajero
                billetes_entregados = {}
                for denominacion, cantidad in saldo_cajero.items():
                    if monto_retiro >= denominacion:
                        cantidad_entregada = min(monto_retiro // denominacion, cantidad)
                        monto_retiro -= cantidad_entregada * denominacion
                        saldo_cajero[denominacion] -= cantidad_entregada
                        billetes_entregados[denominacion] = cantidad_entregada

                # Imprimir el saldo y los billetes entregados
                print("Saldo cuenta =", saldo_usuario)
                print("Saldo cajero =", sum(denominacion * cantidad for denominacion, cantidad in saldo_cajero.items()))

                for denominacion, cantidad_entregada in billetes_entregados.items():
                    print("billetes {} = {}".format(denominacion, cantidad_entregada))

                break

    else:
        intentos += 1
        print("Clave inválida.")

        if intentos == intentos_maximos:
            print("Tarjeta bloqueada.")
            break

    continuar = input("¿Desea realizar otra transacción? (S/r): ")
    if continuar.upper() != "r":
        break
      