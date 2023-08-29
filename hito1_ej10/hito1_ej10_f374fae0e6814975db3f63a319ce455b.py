def cajero(usuario, clave, monto_retiro):
    saldo_cuenta = 100000
    saldo_cajero = 1000000
    intentos = 0

    if usuario == "10334151" and clave == "1803":
        saldo_cuenta = 100000
        print("Bienvenido/a. Su saldo actual es:", saldo_cuenta)

        if monto_retiro <= 0:
            print("Monto no permitido.")
        elif monto_retiro > saldo_cuenta or monto_retiro > saldo_cajero:
            print("Monto no permitido. Saldo insuficiente.")
        else:
            saldo_cuenta -= monto_retiro
            saldo_cajero -= monto_retiro

            print("saldo cuenta={}".format(saldo_cuenta))
            print("saldo cajero={}".format(saldo_cajero))

    else:
        intentos += 1
        print("Clave inválida.")

        if intentos == 3:
            print("Tarjeta bloqueada.")

# Ejemplo de uso
usuario = input("Ingrese su usuario: ")
clave = input("Ingrese su clave: ")
monto_retiro = int(input("Ingrese el monto a retirar: "))

cajero(usuario, clave, monto_retiro)