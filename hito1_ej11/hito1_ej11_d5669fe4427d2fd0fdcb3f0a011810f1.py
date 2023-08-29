#Cajero Automático
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40
saldo_cuenta = 100000
saldo_cajero = 1000000

intentos = 0
usuario_valido = False

while intentos < 3 and not usuario_valido:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        usuario_valido = True
    else:
        print("Clave inválida")
        intentos += 1

if intentos == 3:
    print("Tarjeta bloqueada")
else:
    while True:
        monto = int(input("Ingrese el monto a retirar: "))

        if monto > saldo_cuenta:
            print("Monto no permitido")
        else:
            billetes_20000_retirados = min(monto // 20000, billetes_20000)
            monto -= billetes_20000_retirados * 20000
            billetes_10000_retirados = min(monto // 10000, billetes_10000)
            monto -= billetes_10000_retirados * 10000
            billetes_5000_retirados = min(monto // 5000, billetes_5000)
            monto -= billetes_5000_retirados * 5000

            saldo_cuenta -= (billetes_20000_retirados * 20000 +
                             billetes_10000_retirados * 10000 +
                             billetes_5000_retirados * 5000)
            saldo_cajero -= (billetes_20000_retirados * 20000 +
                             billetes_10000_retirados * 10000 +
                             billetes_5000_retirados * 5000)

            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", saldo_cajero)
            print("Billetes 20000 =", billetes_20000_retirados)
            print("Billetes 10000 =", billetes_10000_retirados)
            print("Billetes 5000 =", billetes_5000_retirados)

        continuar = input("¿Desea realizar otro retiro? (S/N): ")

        if continuar.upper() != "S":
            break



      