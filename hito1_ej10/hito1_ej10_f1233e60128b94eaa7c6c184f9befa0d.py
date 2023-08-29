# Saldo inicial en el cajero
saldo_cajero = 1000000

# Datos del usuario autorizado
usuario_autorizado = "10334151"
clave_autorizada = "1803"
saldo_usuario = 100000

# Contadores para controlar los intentos de ingreso de clave incorrecta
intentos_clave = 0

# Ciclo principal del programa
while True:
    # Solicitar al usuario ingresar usuario y clave
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    # Verificar si la clave y el usuario son correctos
    if usuario == usuario_autorizado and clave == clave_autorizada:
        # Reiniciar contador de intentos fallidos
        intentos_clave = 0

        # Solicitar al usuario el monto a retirar
        monto_retiro = float(input("Ingrese el monto a retirar: "))

        # Verificar si el monto es válido
        if monto_retiro <= saldo_usuario:
            # Actualizar saldos
            saldo_usuario -= monto_retiro
            saldo_cajero -= monto_retiro

            # Imprimir nuevos saldos
            print("Saldo cuenta:", saldo_usuario)
            print("Saldo cajero:", saldo_cajero)
        else:
            print("Monto no permitido")
    else:
        print("Clave inválida")

        # Incrementar contador de intentos fallidos
        intentos_clave += 1

        # Verificar si se han realizado 3 intentos fallidos
        if intentos_clave >= 3:
            print("Tarjeta bloqueada")
            break

    # Preguntar al usuario si desea realizar otra transacción
    opcion = input("¿Desea realizar otra transacción? (N para salir): ")
    if opcion == "N":
        break
