#Cajero Automático
saldo_inicial = 1000000
saldo_cuenta = 100000
saldo_cajero = saldo_inicial - saldo_cuenta

intentos = 0
bloqueado = False

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Inicio de sesión exitoso.")
        break
    else:
        intentos += 1
        if intentos >= 3:
            bloqueado = True
            break
        print("Clave inválida. Intente nuevamente.")

if bloqueado:
    print("Tarjeta bloqueada.")
else:
    while True:
        if saldo_cuenta == 0:
            print("No hay saldo disponible en su cuenta.")
            break

        try:
            monto_retiro = float(input("Ingrese el monto a retirar: "))
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")
            continue

        if monto_retiro <= 0:
            print("Monto no permitido. Intente nuevamente.")
            continue
        elif monto_retiro > saldo_cuenta or monto_retiro > saldo_cajero:
            print("Saldo insuficiente. Intente nuevamente.")
            continue

        saldo_cuenta -= monto_retiro
        saldo_cajero -= monto_retiro

        print("Retiro exitoso.")
        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)

        opcion = input("¿Desea realizar otra transacción? (N para salir): ")
        if opcion.upper() == "N":
            break

print("¡Gracias por utilizar nuestro cajero!")
