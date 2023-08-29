#Cajero Automático
billetes_disponibles = {
    20000: 20,   # Cantidad de billetes de 20.000 disponibles
    10000: 40,   # Cantidad de billetes de 10.000 disponibles
    5000: 40     # Cantidad de billetes de 5.000 disponibles
}

saldo_cajero = sum(billete * cantidad for billete, cantidad in billetes_disponibles.items())  # Saldo inicial del cajero
usuario_valido = "10334151"
clave_valida = "1803"
saldo_usuario = 100000  # Saldo inicial del usuario

intentos_fallidos = 0  # Contador de intentos fallidos de ingreso

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == usuario_valido and clave == clave_valida:
        intentos_fallidos = 0  # Reiniciar contador de intentos fallidos

        monto = float(input("Ingrese el monto a retirar: "))

        if monto <= saldo_usuario:
            if monto <= saldo_cajero:
                billetes_entregados = {}  # Diccionario para almacenar la cantidad de billetes entregados

                for billete, cantidad_disponible in billetes_disponibles.items():
                    cantidad_entregada = min(int(monto / billete), cantidad_disponible)
                    billetes_entregados[billete] = cantidad_entregada
                    monto -= billete * cantidad_entregada

                    billetes_disponibles[billete] -= cantidad_entregada

                saldo_usuario -= (monto + sum(billete * cantidad for billete, cantidad in billetes_entregados.items()))
                saldo_cajero -= sum(billete * cantidad for billete, cantidad in billetes_entregados.items())

                print("Retiro exitoso")
                print("Saldo cuenta:", saldo_usuario)
                print("Saldo cajero:", saldo_cajero)

                for billete, cantidad_entregada in billetes_entregados.items():
                    print("Billetes", billete, "=", cantidad_entregada)

            else:
                print("Monto no permitido. El cajero no dispone de suficiente dinero.")
        else:
            print("Monto no permitido. Saldo insuficiente en la cuenta del usuario.")
    else:
        intentos_fallidos += 1
        print("Clave inválida")

        if intentos_fallidos >= 3:
            print("Tarjeta bloqueada")
            break

    opcion = input("¿Desea realizar otra transacción? (N para salir): ")
    if opcion.upper() == "N":
        break
