saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0
clave_valida = False

while intentos_fallidos < 3:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        clave_valida = True
        break
    else:
        intentos_fallidos += 1
        print("Clave inválida. Intentos fallidos:", intentos_fallidos)

if not clave_valida:
    print("Tarjeta bloqueada. Ha alcanzado el límite de intentos.")
else:
    while True:
        monto_retiro = int(input("Ingrese el monto a retirar: "))

        if monto_retiro % 5000 != 0:
            print("Monto no permitido. El monto debe ser múltiplo de 5000.")
        elif monto_retiro > saldo_cuenta:
            print("Fondos insuficientes en la cuenta.")
        elif monto_retiro > saldo_cajero:
            print("Cajero sin suficientes fondos para realizar el retiro.")
        else:
            saldo_cuenta -= monto_retiro
            saldo_cajero -= monto_retiro

            billetes_20000 = monto_retiro // 20000
            monto_retiro %= 20000
            billetes_10000 = monto_retiro // 10000
            monto_retiro %= 10000
            billetes_5000 = monto_retiro // 5000

            print("Saldo en cuenta =", saldo_cuenta)
            print("Saldo en cajero =", saldo_cajero)
            print("Billetes 20000 =", billetes_20000)
            print("Billetes 10000 =", billetes_10000)
            print("Billetes 5000 =", billetes_5000)
            break
