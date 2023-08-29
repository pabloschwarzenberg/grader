def cajero():
    saldo_cuenta = 100000
    saldo_cajero = {
        20000: 20,
        10000: 40,
        5000: 40
    }

    usuario = input("Ingrese el número de usuario: ")
    clave = input("Ingrese la clave: ")

    if usuario == "10334151" and clave == "1803":
        intentos = 0
        while intentos < 3:
            monto = float(input("Ingrese el monto a retirar: "))

            if monto > saldo_cuenta:
                print("Saldo insuficiente")
                break

            if monto % 5000 != 0:
                print("Monto no permitido")
                break

            if monto > saldo_cajero_total(saldo_cajero):
                print("Cajero sin fondos")
                break

            saldo_cuenta -= monto
            billetes_retirados = distribuir_billetes(monto, saldo_cajero)

            print("Saldo cuenta:", saldo_cuenta)
            print("Saldo cajero:", saldo_cajero_total(saldo_cajero))
            print("Billetes retirados:")
            for billete, cantidad in billetes_retirados.items():
                print("Billetes", billete, "=", cantidad)

            break
        else:
            print("Tarjeta bloqueada")
    else:
        print("Clave inválida")

def saldo_cajero_total(saldo_cajero):
    total = 0
    for billete, cantidad in saldo_cajero.items():
        total += billete * cantidad
    return total

def distribuir_billetes(monto, saldo_cajero):
    billetes_retirados = {}

    for billete, cantidad in sorted(saldo_cajero.items(), reverse=True):
        if monto >= billete and cantidad > 0:
            cantidad_retirada = min(monto // billete, cantidad)
            billetes_retirados[billete] = cantidad_retirada
            monto -= billete * cantidad_retirada
            saldo_cajero[billete] -= cantidad_retirada

    return billetes_retirados

cajero()

      