#Cajero Automático
# Saldo inicial en el cajero y la cuenta corriente
saldo_cajero = 1000000
saldo_cuenta = 100000

# Usuario y clave permitidos
usuario_permitido = "10334151"
clave_permitida = "1803"

# Contadores de intentos fallidos y bloqueo de tarjeta
intentos_fallidos = 0
bloqueo_tarjeta = False

while True:
    # Pedir al usuario que ingrese su usuario y clave
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    # Verificar si el usuario y la clave son válidos
    if usuario == usuario_permitido and clave == clave_permitida:
        # Reiniciar los intentos fallidos y permitir el acceso
        intentos_fallidos = 0
        acceso_permitido = True
    else:
        intentos_fallidos += 1
        if intentos_fallidos >= 3:
            bloqueo_tarjeta = True
            print("Tarjeta bloqueada. Contacte al banco.")
            break
        else:
            print("Clave inválida. Intente nuevamente.")
            continue

    # Verificar si la tarjeta está bloqueada
    if bloqueo_tarjeta:
        break

    # Pedir al usuario que ingrese el monto a retirar
    monto_retiro = float(input("Ingrese el monto a retirar: "))

    # Verificar si el monto es válido
    if monto_retiro <= 0 or monto_retiro > saldo_cuenta:
        print("Monto no permitido.")
    else:
        # Actualizar los saldos
        saldo_cuenta -= monto_retiro
        saldo_cajero -= monto_retiro

        # Imprimir los nuevos saldos
        print("saldo cuenta =", saldo_cuenta)
        print("saldo cajero =", saldo_cajero)

    # Preguntar al usuario si desea realizar otra transacción
    continuar = input("¿Desea realizar otra transacción? (S/N): ")
    if continuar.upper() != "S":
        break      