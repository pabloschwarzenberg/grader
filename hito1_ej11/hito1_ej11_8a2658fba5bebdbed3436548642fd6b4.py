saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 0
usuario = 10334151
clave = 1803

billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

while intentos < 3:
    input_usuario = int(input("Ingrese su número de usuario: "))
    input_clave = int(input("Ingrese su clave: "))

    if input_usuario == usuario and input_clave == clave:
        monto_retiro = int(input("Ingrese el monto a retirar: "))
        if monto_retiro > saldo_cuenta or monto_retiro <= 0:
            print("Monto no permitido")
        else:
            billetes_20000_entregados = min(monto_retiro // 20000, billetes_20000)
            monto_retiro -= billetes_20000_entregados * 20000
            billetes_10000_entregados = min(monto_retiro // 10000, billetes_10000)
            monto_retiro -= billetes_10000_entregados * 10000
            billetes_5000_entregados = min(monto_retiro // 5000, billetes_5000)
            monto_retiro -= billetes_5000_entregados * 5000

            if monto_retiro > 0:
                print("No se pueden entregar billetes para el monto restante:", monto_retiro)
            else:
                saldo_cuenta -= (billetes_20000_entregados * 20000) + (billetes_10000_entregados * 10000) + (billetes_5000_entregados * 5000)
                saldo_cajero -= (billetes_20000_entregados * 20000) + (billetes_10000_entregados * 10000) + (billetes_5000_entregados * 5000)

                print("Saldo cuenta =", saldo_cuenta)
                print("Saldo cajero =", saldo_cajero)
                print("Billetes 20000 =", billetes_20000_entregados)
                print("Billetes 10000 =", billetes_10000_entregados)
                print("Billetes 5000 =", billetes_5000_entregados)
        break
    else:
        intentos += 1
        print("Clave inválida")

if intentos == 3:
    print("Tarjeta bloqueada")
