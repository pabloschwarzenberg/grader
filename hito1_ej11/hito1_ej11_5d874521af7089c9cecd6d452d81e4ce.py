saldo_inicial = 1000000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40
intentos = 0
clave_valida = False

while intentos < 3 and not clave_valida:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        clave_valida = True
    else:
        print("Clave inválida")
        intentos += 1

if not clave_valida:
    print("Tarjeta bloqueada")
else:
    while saldo_inicial > 0:
        try:
            monto = int(input("Ingrese el monto a retirar: "))
            if monto <= saldo_inicial:
                if monto > saldo_inicial:
                    print("Monto no permitido")
                else:
                    billetes_retirados_20000 = min(monto // 20000, billetes_20000)
                    monto -= billetes_retirados_20000 * 20000
                    billetes_retirados_10000 = min(monto // 10000, billetes_10000)
                    monto -= billetes_retirados_10000 * 10000
                    billetes_retirados_5000 = min(monto // 5000, billetes_5000)
                    monto -= billetes_retirados_5000 * 5000

                    saldo_inicial -= (billetes_retirados_20000 * 20000 + billetes_retirados_10000 * 10000 + billetes_retirados_5000 * 5000)
                    billetes_20000 -= billetes_retirados_20000
                    billetes_10000 -= billetes_retirados_10000
                    billetes_5000 -= billetes_retirados_5000

                    print("Saldo cuenta =", saldo_inicial)
                    print("Billetes 20000 =", billetes_retirados_20000)
                    print("Billetes 10000 =", billetes_retirados_10000)
                    print("Billetes 5000 =", billetes_retirados_5000)
            else:
                print("Monto no permitido")
                break
        except ValueError:
            print("Error: El monto ingresado no es válido. Por favor, ingrese un número válido.")

    print("Tarjeta bloqueada")
