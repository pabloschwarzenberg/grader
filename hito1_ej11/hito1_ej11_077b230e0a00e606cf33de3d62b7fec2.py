#Cajero Automático
def cajero_automatico(monto):
    saldo = {
        20000: 20,
        10000: 40,
        5000: 40
    }

    billetes_entregados = {}
    for denominacion, cantidad_disponible in saldo.items():
        if cantidad_disponible == 0:
            continue

        cantidad_billetes = min(monto // denominacion, cantidad_disponible)
        monto -= cantidad_billetes * denominacion
        saldo[denominacion] -= cantidad_billetes
        billetes_entregados[denominacion] = cantidad_billetes

    if monto > 0:
        return "No se puede retirar el monto solicitado."

    return billetes_entregados


monto_retirar = int(input("Ingrese el monto a retirar: "))

resultado = cajero_automatico(monto_retirar)

if isinstance(resultado, dict):
    print("Billetes entregados:")
    for denominacion, cantidad in resultado.items():
        print("Billetes de", denominacion, "=", cantidad)
else:
    print(resultado)
      