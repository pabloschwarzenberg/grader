#Cajero Automatico
saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Acceso permitido")
        break
    else:
        intentos_fallidos += 1
        print("Clave inválida")
        if intentos_fallidos == 3:
            print("Tarjeta bloqueada")
            exit()

while True:
    monto_retiro = float(input("Ingrese el monto a retirar: "))

    if monto_retiro <= 0 or monto_retiro > saldo_cuenta:
        print("Monto no permitido")
    else:
        saldo_cuenta -= monto_retiro
        saldo_cajero -= monto_retiro
        print(f"Saldo cuenta: {saldo_cuenta}")
        print(f"Saldo cajero: {saldo_cajero}")

    continuar = input("¿Desea realizar otra transacción? (N para salir): ")
    if continuar.upper() != "N":
        break
