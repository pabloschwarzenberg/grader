saldo_cuenta = 100000
saldo_cajero = 1000000

billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

intentos_fallidos = 0

usuario_valido = 10334151
clave_valida = 1803

while True:
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario == usuario_valido and clave == clave_valida:
        break
    else:
        print("Clave inválida")
        intentos_fallidos += 1

    if intentos_fallidos >= 3:
        print("Tarjeta bloqueada")
        exit()

while True:
    monto_retiro = float(input("Ingrese el monto a retirar: "))

    if monto_retiro > saldo_cuenta:
        print("Monto no permitido")
    else:
        billetes_20000_retiro = min(monto_retiro // 20000, billetes_20000)
        monto_retiro -= billetes_20000_retiro * 20000

        billetes_10000_retiro = min(monto_retiro // 10000, billetes_10000)
        monto_retiro -= billetes_10000_retiro * 10000

        billetes_5000_retiro = min(monto_retiro // 5000, billetes_5000)
        monto_retiro -= billetes_5000_retiro * 5000

        saldo_cuenta -= (billetes_20000_retiro * 20000) + (billetes_10000_retiro * 10000) + (billetes_5000_retiro * 5000)
        saldo_cajero -= (billetes_20000_retiro * 20000) + (billetes_10000_retiro * 10000) + (billetes_5000_retiro * 5000)

        print("Billetes 20000 =", int(billetes_20000_retiro))
        print("Billetes 10000 =", int(billetes_10000_retiro))
        print("Billetes 5000 =", int(billetes_5000_retiro))
        break

print("Saldo cuenta =", saldo_cuenta)
print("Saldo cajero =", saldo_cajero)
