#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        intentos_fallidos = 0
        print("Inicio de sesión exitoso.")

        while True:
            monto = float(input("Ingrese el monto a retirar: "))

            if monto <= saldo_cuenta:
                if monto <= saldo_cajero:
                    saldo_cuenta -= monto
                    saldo_cajero -= monto
                    print("Retiro exitoso.")
                    print(f"Saldo cuenta: {saldo_cuenta}")
                    print(f"Saldo cajero: {saldo_cajero}")
                else:
                    print("Monto no permitido. El cajero no tiene suficiente saldo.")
            else:
                print("Monto no permitido. El saldo de la cuenta no es suficiente.")

            continuar = input("¿Desea realizar otro retiro? (S/N): ")
            if continuar.upper() != "S":
                break
    else:
        intentos_fallidos += 1
        print("Clave inválida.")

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada.")
            break
