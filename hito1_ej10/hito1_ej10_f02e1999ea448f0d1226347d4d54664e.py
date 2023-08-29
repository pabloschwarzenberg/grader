saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Bienvenido(a) al cajero automático.")
        break
    else:
        intentos_fallidos += 1
        if intentos_fallidos >= 3:
            print("Tarjeta bloqueada. Ha excedido el número máximo de intentos.")
            exit()
        else:
            print("Clave inválida. Por favor, intente nuevamente.")

while True:
    monto_retiro = float(input("Ingrese el monto a retirar: "))

    if monto_retiro > saldo_cuenta or monto_retiro <= 0:
        print("Monto no permitido. Por favor, ingrese un monto válido.")
    else:
        saldo_cuenta -= monto_retiro
        saldo_cajero -= monto_retiro

        print("Retiro exitoso.")
        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break

print("Gracias por utilizar nuestro cajero automático. ¡Hasta luego!")

