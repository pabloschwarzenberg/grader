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
    print("Bienvenido al cajero automático")
    usuario_ingresado = input("Ingrese su usuario: ")
    clave_ingresada = input("Ingrese su clave: ")
    if usuario_ingresado == usuario and clave_ingresada == clave:
        intentos = 0
        monto = int(input("Ingrese el monto a retirar: "))
        if monto > saldo_cuenta or monto > saldo_cajero:
            print("Monto no permitido")
        else:
            saldo_cuenta -= monto
            saldo_cajero -= monto
            print("Saldo cuenta={}".format(saldo_cuenta))
            print("Saldo cajero={}".format(saldo_cajero))
            b20000 = min(billetes_20000, monto // 20000)
            monto -= b20000 * 20000
            billetes_20000 -= b20000
            b10000 = min(billetes_10000, monto // 10000)
            monto -= b10000 * 10000
            billetes_10000 -= b10000
            b5000 = min(billetes_5000, monto // 5000)
            monto -= b5000 * 5000
            billetes_5000 -= b5000
            print("Billetes 20000={}".format(b20000))
            print("Billetes 10000={}".format(b10000))
            print("Billetes 5000={}".format(b5000))
    else:
        intentos += 1
        if intentos == 3:
            print("Tarjeta bloqueada")
            break
        else:
            print("Clave inválida")
    continuar = input("¿Desea realizar otra operación? (N para salir): ")
    if continuar != "N":
        break
