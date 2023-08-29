saldo_inicial = 1000000
billetes_disponibles = {
    20000: 20,
    10000: 40,
    5000: 40
}
intentos_fallidos = 0

def validar_clave(clave):
    return clave == "1803"

def hacer_retiro(saldo, monto):
    billetes_retirados = {
        20000: 0,
        10000: 0,
        5000: 0
    }

    for billete in sorted(billetes_disponibles.keys(), reverse=True):
        cantidad_billetes = min(monto // billete, billetes_disponibles[billete])
        monto -= billete * cantidad_billetes
        billetes_disponibles[billete] -= cantidad_billetes
        billetes_retirados[billete] = cantidad_billetes

    if monto == 0:
        return saldo - monto, billetes_retirados
    else:
        return None, billetes_retirados

# Pedir usuario y clave
usuario = input("Usuario: ")
clave = input("Clave: ")

# Verificar el usuario y la clave
if usuario == "10334151" and validar_clave(clave):
    saldo_cuenta = 100000
    saldo_cajero = saldo_inicial
    print("Bienvenido,", usuario)

    monto = int(input("Ingrese el monto a retirar: "))

    # Verificar el monto a retirar
    if monto <= 0:
        print("Monto no permitido")
    else:
        # Realizar el retiro
        nuevo_saldo_cuenta, billetes_retirados = hacer_retiro(saldo_cuenta, monto)

        if nuevo_saldo_cuenta is None:
            print("Saldo insuficiente")
        else:
            saldo_cuenta = nuevo_saldo_cuenta
            saldo_cajero -= monto
            print("Retiro exitoso")
            print("saldo cuenta =", saldo_cuenta)
            print("saldo cajero =", saldo_cajero)
            for billete, cantidad in billetes_retirados.items():
                print("billetes", billete, "=", cantidad)
else:
    print("Tarjeta bloqueada")