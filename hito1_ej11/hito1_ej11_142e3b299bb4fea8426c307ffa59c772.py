#Cajero Automático
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

def imprimir_saldos():
    print("Saldo actual del cajero:")
    print("Billetes de 20.000:", billetes_20000)
    print("Billetes de 10.000:", billetes_10000)
    print("Billetes de 5.000:", billetes_5000)

def realizar_retiro(monto):
    imprimir_saldos()

    if monto <= 0:
        print("Monto inválido.")
        return

    if monto > (billetes_20000 * 20000 + billetes_10000 * 10000 + billetes_5000 * 5000):
        print("Saldo insuficiente en el cajero.")
        return

    # Calcula la cantidad de billetes necesarios para el retiro
    billetes_20000_retirados = min(monto // 20000, billetes_20000)
    monto -= billetes_20000_retirados * 20000

    billetes_10000_retirados = min(monto // 10000, billetes_10000)
    monto -= billetes_10000_retirados * 10000

    billetes_5000_retirados = min(monto // 5000, billetes_5000)
    monto -= billetes_5000_retirados * 5000

    # Actualiza los saldos de los billetes
    billetes_20000 -= billetes_20000_retirados
    billetes_10000 -= billetes_10000_retirados
    billetes_5000 -= billetes_5000_retirados

    print("Monto retirado:", monto)
    print("Billetes de 20.000:", billetes_20000_retirados)
    print("Billetes de 10.000:", billetes_10000_retirados)
    print("Billetes de 5.000:", billetes_5000_retirados)
    imprimir_saldos()

if __name__ == "__main__":
    while True:
        print("1. Realizar retiro")
        print("2. Salir")
        opcion = int(input("Ingrese su opción: "))

        if opcion == 1:
            monto = int(input("Ingrese el monto a retirar: "))
            realizar_retiro(monto)
        elif opcion == 2:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
        print()