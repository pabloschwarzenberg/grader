#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40
intentos = 0

usuario_valido = 10334151
clave_valida = 1803

while intentos < 3:
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario == usuario_valido and clave == clave_valida:
        monto_retiro = int(input("Ingrese el monto a retirar: "))

        if monto_retiro > saldo_cuenta:
            print("Monto no permitido")
        else:
            if monto_retiro > saldo_cajero:
                print("Cajero sin fondos suficientes")
            else:
                billetes_20000_retirados = min(monto_retiro // 20000, billetes_20000)
                monto_retiro -= billetes_20000_retirados * 20000
                billetes_10000_retirados = min(monto_retiro // 10000, billetes_10000)
                monto_retiro -= billetes_10000_retirados * 10000
                billetes_5000_retirados = min(monto_retiro // 5000, billetes_5000)
                monto_retiro -= billetes_5000_retirados * 5000

                saldo_cuenta -= (billetes_20000_retirados * 20000 + billetes_10000_retirados * 10000 + billetes_5000_retirados * 5000)
                saldo_cajero -= (billetes_20000_retirados * 20000 + billetes_10000_retirados * 10000 + billetes_5000_retirados * 5000)
                billetes_20000 -= billetes_20000_retirados
                billetes_10000 -= billetes_10000_retirados
                billetes_5000 -= billetes_5000_retirados

                print("Saldo cuenta =", saldo_cuenta)
                print("Saldo cajero =", saldo_cajero)
                print("Billetes 20000 =", billetes_20000_retirados)
                print("Billetes 10000 =", billetes_10000_retirados)
                print("Billetes 5000 =", billetes_5000_retirados)
        break
    else:
        print("Clave inválida")
        intentos += 1

if intentos == 3:
    print("Tarjeta bloqueada")
      