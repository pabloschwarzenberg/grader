def validar_usuario(usuario, clave):
    return usuario == "10334151" and clave == "1803"

def retirar_dinero(saldo_cuenta, monto):
    if monto > saldo_cuenta or monto % 10000 != 0:
        print("Monto no permitido")
        return saldo_cuenta, {}

    billetes_entregados = {
        20000: 0,
        10000: 0,
        5000: 0
    }

    saldo_cuenta -= monto

    saldo_cajero = {
        20000: 20,
        10000: 40,
        5000: 40
    }

    for billete in sorted(billetes_entregados.keys(), reverse=True):
        cantidad_billetes = min(monto // billete, saldo_cajero[billete])
        monto -= cantidad_billetes * billete
        billetes_entregados[billete] = cantidad_billetes
        saldo_cajero[billete] -= cantidad_billetes

    return saldo_cuenta, billetes_entregados

saldo_cuenta = 100000
intentos = 0

while True:
    usuario = input("Ingrese el usuario: ")
    clave = input("Ingrese la clave: ")

    if validar_usuario(usuario, clave):
        while True:
            monto = int(input("Ingrese el monto a retirar (múltiplo de 10.000): "))
            if monto > 0:
                saldo_cuenta, billetes_entregados = retirar_dinero(saldo_cuenta, monto)
                if billetes_entregados:
                    print("Billetes entregados:")
                    for billete, cantidad in billetes_entregados.items():
                        if cantidad > 0:
                            print(f"Billetes {billete}: {cantidad}")
                print(f"Saldo cuenta: {saldo_cuenta}")
                print("Saldo cajero:")
                for billete, cantidad in saldo_cajero.items():
