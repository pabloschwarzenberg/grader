def agregar_producto(carro, producto, cantidad):
    if producto in carro:
        carro[producto] += cantidad
    else:
        carro[producto] = cantidad

def imprimir_productos(carro):
    print("Productos en el carro:")
    for producto, cantidad in carro.items():
        print(f"Producto {producto}: {cantidad} unidades")

def calcular_descuento(carro):
    total_descuento = 0

    # Descuento del 20% para los productos 1, 2 y 3
    if '1' in carro and '2' in carro and '3' in carro:
        descuento = 0.2 * (carro['1'] + carro['2'] + carro['3'])
        total_descuento += descuento

    # Descuento del 15% para los productos 4 y 5
    if '4' in carro and '5' in carro:
        descuento = 0.15 * (carro['4'] + carro['5'])
        total_descuento += descuento

    return total_descuento

def hacer_checkout(carro):
    descuento = calcular_descuento(carro)
    total = sum(carro.values()) - descuento
    print(f"Total a pagar: {round(total, 1)}")

# Función principal
def programa_carro():
    carro = {}

    while True:
        orden = input("Ingrese una orden (agregar, ver, checkout): ")

        if orden == "agregar":
            producto, cantidad = input("Ingrese el producto y la cantidad separados por coma: ").split(',')
            agregar_producto(carro, producto, int(cantidad))
        elif orden == "ver":
            imprimir_productos(carro)
        elif orden == "checkout":
            hacer_checkout(carro)
            break
        else:
            print("Orden inválida. Por favor, intente nuevamente.")

programa_carro()
