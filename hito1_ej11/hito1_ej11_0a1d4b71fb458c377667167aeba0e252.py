#Cajero Automático
saldo_cajero = 1000000
saldo_cuenta = 100000
usuario = "10334151"
clave = "1803"
intentos = 0
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

while True:
    usuario_ingresado = input("Ingresa tu usuario: ")
    clave_ingresada = input("Ingresa tu clave: ")
    if usuario_ingresado == usuario and clave_ingresada == clave:
        monto = int(input("Ingresa el monto a retirar: "))
        if 0 < monto <= saldo_cuenta and monto <= saldo_cajero:
            saldo_cuenta -= monto
            saldo_cajero -= monto
            billetes_20000_retirados = min(monto // 20000, billetes_20000)
            monto -= billetes_20000_retirados * 20000
            billetes_20000 -= billetes_20000_retirados
            billetes_10000_retirados = min(monto // 10000, billetes_10000)
            monto -= billetes_10000_retirados * 10000
            billetes_10000 -= billetes_10000_retirados
            billetes_5000_retirados = min(monto // 5000, billetes_5000)
            monto -= billetes_5000_retirados * 5000
            billetes_5000 -= billetes_5000_retirados
            print("saldo cuenta =", saldo_cuenta)
            print("saldo cajero =", saldo_cajero)
            print("billetes 20000 =", billetes_20000_retirados)
            print("billetes 10000 =", billetes_10000_retirados)
            print("billetes 5000 =", billetes_5000_retirados)
        else:
            print("monto no permitido")
    else:
        print("clave invalida")
        intentos += 1
        if intentos == 3:
            print("tarjeta bloqueada")
            break
    continuar = input("¿Deseas continuar? (N para salir): ")
    if continuar != "N":
        break
