def cajero():
    usuario_valido = 10334151
    clave_valida = 1803
    saldo_inicial = 100000
    saldo_cajero = 1000000

    intentos = 0

    while intentos < 3:
        usuario = int(input("Ingrese su número de usuario: "))
        clave = int(input("Ingrese su clave: "))

        if usuario == usuario_valido and clave == clave_valida:
            monto_retiro = float(input("Ingrese el monto a retirar: "))

            if monto_retiro > saldo_inicial:
                print("Monto no permitido. Saldo insuficiente.")
            elif monto_retiro > saldo_cajero:
                print("Monto no permitido. Saldo insuficiente en el cajero.")
            else:
                saldo_inicial -= monto_retiro
                saldo_cajero -= monto_retiro
                print("Retiro exitoso.")
                print("Nuevo saldo en la cuenta corriente: ", saldo_inicial)
                print("Nuevo saldo en el cajero: ", saldo_cajero)
                break
        else:
            print("Clave inválida.")
            intentos += 1

    if intentos == 3:
        print("Tarjeta bloqueada.")


# Ejemplo de uso
cajero()
