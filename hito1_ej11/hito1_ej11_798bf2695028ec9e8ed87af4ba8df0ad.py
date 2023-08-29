#Cajero Automático
def distribuir_billetes(monto):
    saldo = {
        20000: 20,
        10000: 40,
        5000: 40
    }
    cantidad_billetes = {
        20000: 0,
        10000: 0,
        5000: 0
    }

    for billete, cantidad in saldo.items():
        if monto >= billete:
            cantidad_billetes[billete] = min(monto // billete, cantidad)
            monto -= billete * cantidad_billetes[billete]

    if monto == 0:
        for billete, cantidad in cantidad_billetes.items():
            if cantidad > 0:
                print("billetes {}={}".format(billete, cantidad))
        return True
    else:
        return False

monto_solicitado = int(input("Ingrese el monto que desea retirar: "))
if distribuir_billetes(monto_solicitado):
    print("Retiro exitoso.")
else:
    print("No se puede realizar el retiro. Por favor, ingrese un monto válido.")
