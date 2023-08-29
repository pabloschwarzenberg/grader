saldo_cuenta = 100000
saldo_cajero = 1000000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

usuario_valido = "10334151"
clave_valida = "1803"
intentos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == usuario_valido and clave == clave_valida:
        print("Acceso concedido.")
        break
    else:
        intentos += 1
        print("Clave inválida.")

    if intentos >= 3:
        print("Tarjeta bloqueada.")
        exit()

while True:
    try:
        monto_retiro = int(input("Ingrese el monto a retirar: "))
        if monto_retiro <= 0:
            raise ValueError
        break
    except ValueError:
        print("Monto no permitido. Ingrese un monto válido.")

if monto_retiro > saldo_cuenta:
    print("Saldo insuficiente.")
else:
    if monto_retiro > saldo_cajero:
        print("Cajero sin fondos suficientes.")
    else:
        billetes_entregados = []
        while monto_retiro > 0:
            if monto_retiro >= 20000 and billetes_20000 > 0:
                cantidad_billetes = min(monto_retiro // 20000, billetes_20000)
                monto_retiro -= cantidad_billetes * 20000
                saldo_cajero -= cantidad_billetes * 20000
                billetes_20000 -= cantidad_billetes
                billetes_entregados.append(f"billetes 20000={cantidad_billetes}")
            elif monto_retiro >= 10000 and billetes_10000 > 0:
                cantidad_billetes = min(monto_retiro // 10000, billetes_10000)
                monto_retiro -= cantidad_billetes * 10000
                saldo_cajero -= cantidad_billetes * 10000
                billetes_10000 -= cantidad_billetes
                billetes_entregados.append(f"billetes 10000={cantidad_billetes}")
            elif monto_retiro >= 5000 and billetes_5000 > 0:
                cantidad_billetes = min(monto_retiro // 5000, billetes_5000)
                monto_retiro -= cantidad_billetes * 5000
                saldo_cajero -= cantidad_billetes * 5000
                billetes_5000 -= cantidad_billetes
                billetes_entregados.append(f"billetes 5000={cantidad_billetes}")
            else:
                break

        saldo_cuenta -= monto_retiro

        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)
        print("Billetes entregados:")
        for billete in billetes_entregados:
            print(billete)
