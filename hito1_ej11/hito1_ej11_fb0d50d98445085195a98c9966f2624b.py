#Cajero Automático
saldo_cajero = {
    "billetes_20000": 20,
    "billetes_10000": 40,
    "billetes_5000": 40
}

saldo_inicial = 100000

usuario_valido = "10334151"
clave_valida = "1803"
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == usuario_valido and clave == clave_valida:
        saldo_cuenta = saldo_inicial
        break
    else:
        print("Clave inválida.")
        intentos_fallidos += 1

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada.")
            exit()

while True:
    monto_retiro = float(input("Ingrese el monto a retirar: "))

    if monto_retiro > saldo_cuenta or monto_retiro < 0:
        print("Monto no permitido.")
    else:
        billetes_20000 = min(int(monto_retiro / 20000), saldo_cajero["billetes_20000"])
        monto_retiro -= billetes_20000 * 20000

        billetes_10000 = min(int(monto_retiro / 10000), saldo_cajero["billetes_10000"])
        monto_retiro -= billetes_10000 * 10000

        billetes_5000 = min(int(monto_retiro / 5000), saldo_cajero["billetes_5000"])
        monto_retiro -= billetes_5000 * 5000

        saldo_cuenta -= (billetes_20000 * 20000) + (billetes_10000 * 10000) + (billetes_5000 * 5000)
        saldo_cajero["billetes_20000"] -= billetes_20000
        saldo_cajero["billetes_10000"] -= billetes_10000
        saldo_cajero["billetes_5000"] -= billetes_5000

        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", sum(saldo_cajero.values()))
        print("Billetes 20000 =", billetes_20000)
        print("Billetes 10000 =", billetes_10000)
        print("Billetes 5000 =", billetes_5000)

    opcion = input("¿Desea realizar otro retiro? (N para salir): ")
    if opcion.upper() == "N":
        break


