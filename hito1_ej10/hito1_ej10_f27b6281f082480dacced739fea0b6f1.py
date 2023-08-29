#Cajero Automático
saldo_cajero = 1000000  # Saldo inicial del cajero
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
                saldo_usuario -= monto
                saldo_cajero -= monto
                print("Retiro exitoso")
                print("Saldo cuenta:", saldo_usuario)
                print("Saldo cajero:", saldo_cajero)
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
