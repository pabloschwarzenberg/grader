saldo_cajero = 1000000
saldo_inicial = 100000
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        saldo_cuenta = saldo_inicial
        print("¡Bienvenido!")

        while True:
            monto_retiro = float(input("Ingrese el monto a retirar: "))

            if monto_retiro <= 0:
                print("Monto no permitido. El monto a retirar debe ser mayor a cero.")
            elif monto_retiro > saldo_cuenta:
                print("Monto no permitido. El saldo de su cuenta es insuficiente.")
            else:
                saldo_cuenta -= monto_retiro
                saldo_cajero -= monto_retiro

                print(f"Retiro exitoso. Saldo cuenta: {saldo_cuenta}")
                print(f"Saldo cajero: {saldo_cajero}")

            opcion = input("¿Desea realizar otro retiro? (S/N): ")
            if opcion.upper() != "S":
                break

        break
    else:
        intentos_fallidos += 1
        print("Clave inválida.")

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada.")
            break
