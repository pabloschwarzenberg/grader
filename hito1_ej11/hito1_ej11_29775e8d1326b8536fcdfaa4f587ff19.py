billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

saldo_cajero = billetes_20000 * 20000 + billetes_10000 * 10000 + billetes_5000 * 5000
saldo_cuenta = 100000

intentos = 0
usuario_valido = False

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        usuario_valido = True
        break
    else:
        intentos += 1
        print("Clave inválida")

    if intentos >= 3:
        print("Tarjeta bloqueada")
        exit()

while True:
    monto = float(input("Ingrese el monto a retirar: "))

    if monto <= saldo_cuenta and monto > 0 and monto <= saldo_cajero:
        billetes_20000_entregados = min(billetes_20000, monto // 20000)
        monto -= billetes_20000_entregados * 20000

        billetes_10000_entregados = min(billetes_10000, monto // 10000)
        monto -= billetes_10000_entregados * 10000

        billetes_5000_entregados = min(billetes_5000, monto // 5000)
        monto -= billetes_5000_entregados * 5000

        saldo_cuenta -= (billetes_200
