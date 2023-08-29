saldo_cajero = 1000000  # Saldo inicial del cajero
saldo_usuario = 100000  # Saldo inicial del usuario
intentos_fallidos = 0  # Contador de intentos fallidos de ingreso de clave

# Datos de usuario permitido
usuario_permitido = "10334151"
clave_permitida = "1803"

# Ingreso de usuario y clave
usuario = input("Ingrese su usuario: ")
clave = input("Ingrese su clave: ")

# Validación de usuario y clave
if usuario == usuario_permitido and clave == clave_permitida:
    while True:
        # Ingreso del monto a retirar
        monto_retiro = float(input("Ingrese el monto a retirar: "))

        # Validación del monto a retirar
        if monto_retiro <= 0:
            print("Monto no permitido")
        elif monto_retiro > saldo_usuario:
            print("Saldo insuficiente")
        else:
            # Actualización de saldos
            saldo_cajero -= monto_retiro
            saldo_usuario -= monto_retiro

            # Imprimir nuevos saldos
            print("Nuevo saldo en cuenta corriente:", saldo_usuario)
            print("Nuevo saldo en el cajero:", saldo_cajero)
            break
else:
    print("Clave inválida")
    intentos_fallidos += 1

# Verificación de intentos fallidos
if intentos_fallidos >= 3:
    print("Tarjeta bloqueada")
