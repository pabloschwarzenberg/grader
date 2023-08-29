#Cajero Automático
saldo_cuenta = 100000  # Saldo inicial en la cuenta corriente
saldo_cajero = 1000000  # Saldo inicial en el cajero

intentos = 0  # Contador de intentos de ingreso de clave incorrecta

usuario = "10334151"  # Usuario permitido
clave = "1803"  # Clave permitida

ingreso_usuario = input("Ingrese su usuario: ")  # Entrada de usuario
ingreso_clave = input("Ingrese su clave: ")  # Entrada de clave

if ingreso_usuario == usuario and ingreso_clave == clave:
    intentos = 0  # Reiniciar contador de intentos
    print("Bienvenido!")

    while True:
        monto = float(input("Ingrese el monto a retirar: "))

        if monto <= saldo_cuenta and monto <= saldo_cajero:
            saldo_cuenta -= monto
            saldo_cajero -= monto
            print("Retiro exitoso.")
            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", saldo_cajero)
        else:
            print("Monto no permitido.")

        opcion = input("Desea realizar otro retiro? (S/N): ")
        if opcion.upper() != "S":
            break
else:
    intentos += 1
    print("Clave inválida.")

    if intentos == 3:
        print("Tarjeta bloqueada.")
