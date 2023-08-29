def verificar_usuario(usuario, clave):
    if usuario == 10334151 and clave == 1803:
        return True
    else:
        return False

def realizar_retiro(saldo_cuenta, monto):
    if monto > saldo_cuenta:
        return False
    else:
        saldo_cuenta -= monto
        return saldo_cuenta

def distribuir_billetes(monto):
    billetes_20000 = monto // 20000
    monto %= 20000
    billetes_10000 = monto // 10000
    monto %= 10000
    billetes_5000 = monto // 5000

    return billetes_20000, billetes_10000, billetes_5000

saldo_cajero = 1000000
saldo_cuenta = 100000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

intentos = 0

while True:
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))

    if verificar_usuario(usuario, clave):
        intentos = 0
        monto = int(input("Ingrese el monto a retirar: "))

        if monto <= 0:
            print("Monto no permitido")
        else:
            nuevo_saldo = realizar_retiro(saldo_cuenta, monto)

            if nuevo_saldo is False:
                print("Monto no permitido")
            else:
                saldo_cuenta = nuevo_saldo
                saldo_cajero -= monto
                billetes_20000_retirados, billetes_10000_retirados, billetes_5000_retirados = distribuir_billetes(monto)

                print("saldo cuenta=",saldo_cuenta)
                print("saldo cajero=",saldo_cajero)
                print("billetes 20000=",billetes_20000_retirados)
                print("billetes 10000=",billetes_10000_retirados)
                print("billetes 5000=",billetes_5000_retirados)

                billetes_20000 -= billetes_20000_retirados
                billetes_10000 -= billetes_10000_retirados
                billetes_5000 -= billetes_5000_retirados

    else:
        intentos += 1
        print("Clave inválida")

    if intentos >= 3:
        print("Tarjeta bloqueada")
        break

    continuar = input("¿Desea realizar otra transacción? (S/N): ")
    if continuar.upper() != "S":
        break
      