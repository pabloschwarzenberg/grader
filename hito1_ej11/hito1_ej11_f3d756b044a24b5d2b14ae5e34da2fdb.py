billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

def imprimir_saldo():
    print("Saldo actual del cajero:")
    print("Billetes de 20000:", billetes_20000)
    print("Billetes de 10000:", billetes_10000)
    print("Billetes de 5000:", billetes_5000)

def retirar_dinero(monto):
    if monto <= 0:
        print("El monto debe ser mayor que cero.")
        return

    billetes_entregados = {
        20000: 0,
        10000: 0,
        5000: 0
    }

    while monto >= 2000:
        monto -= 20000
        billetes_20000 -= 1
        billetes_entregados[20000] += 1

    while monto >= 10000 and billetes_10000 > 0:
        monto -= 10000
        billetes_10000 -= 1
        billetes_entregados[10000] += 1

    while monto >= 5000 and billetes_5000 > 0:
        monto -= 5000
        billetes_5000 -= 1
        billetes_entregados[5000] += 1

    if monto == 0:
        print("Retiro exitoso. Billetes entregados:")
    else:
        print("No es posible realizar el retiro. Por favor, intente con otro monto.")

# Ejemplo de uso
imprimir_saldo()

print()

monto_retiro = int(input("Ingrese el monto a retirar: "))
retirar_dinero(monto_retiro)

print()

imprimir_saldo()