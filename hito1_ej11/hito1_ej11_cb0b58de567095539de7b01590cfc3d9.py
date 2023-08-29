#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
billetes_disponibles = {
    20000: 20,
    10000: 40,
    5000: 40
}

def entregar_billetes(monto):
    billetes_entregados = {}

    for denominacion in sorted(billetes_disponibles.keys(), reverse=True):
        cantidad_billetes = min(monto // denominacion, billetes_disponibles[denominacion])
        if cantidad_billetes > 0:
            billetes_entregados[denominacion] = cantidad_billetes
            monto -= cantidad_billetes * denominacion
            billetes_disponibles[denominacion] -= cantidad_billetes

    return billetes_entregados, monto

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Bienvenido(a), usuario 10334151")
        break
    else:
        print("Clave inválida")

    intentos += 1
    if intentos == 3:
        print("Tarjeta bloqueada")
        exit()

while True:
    try:
        monto = int(input("Ingrese el monto a retirar: "))
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")
        continue

    if monto <= 0:
        print("Monto no permitido")
    elif monto > saldo_cuenta:
        print("Saldo insuficiente")
    else:
        billetes_entregados, monto_restante = entregar_billetes(monto)

        if monto_restante == 0:
            saldo_cuenta -= monto
            saldo_cajero -= monto

            print("Retiro exitoso")
            print("Saldo cuenta:", saldo_cuenta)
            print("Saldo cajero:", saldo_cajero)
            for denominacion, cantidad_entregada in billetes_entregados.items():
                print("Billetes", denominacion, "=", cantidad_entregada)
        else:
            print("No se puede retirar el monto solicitado con los billetes disponibles")

    opcion = input("¿Desea realizar otro retiro? (N para salir): ")
    if opcion.upper() == "N":
        break