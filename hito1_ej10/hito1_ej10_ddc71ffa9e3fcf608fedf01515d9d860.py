#Cajero Automático
def cajero_automatico():
    saldo_cuenta = 100000
    saldo_cajero = 1000000
    intentos = 0

    while True:
        user = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")

        if user == "10334151" and clave == "1803":
            print("Bienvenido(a) al cajero automático.")
            break
        else:
            intentos += 1
            print("Clave inválida.")

        if intentos == 3:
            print("Tarjeta bloqueada.")
            return

    while True:
        monto = float(input("Ingrese el monto a retirar: "))

        if monto <= 0:
            print("Monto no permitido.")
        elif monto > saldo_cuenta or monto > saldo_cajero:
            print("Saldo insuficiente en la cuenta o en el cajero.")
        else:
            saldo_cuenta -= monto
            saldo_cajero -= monto
            print("saldo cuenta=", saldo_cuenta)
            print("saldo cajero=", saldo_cajero)
            break
cajero_automatico()