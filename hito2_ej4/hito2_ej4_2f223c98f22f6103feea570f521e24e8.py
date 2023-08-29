def agregar_producto(carro, producto, cantidad):
    if producto in carro:
        carro[producto] += cantidad
    else:
        carro[producto] = cantidad


def mostrar_carro(carro):
    print("Productos en el carro:")
    for producto, cantidad in carro.items():
        print(f"Producto {producto}: {cantidad} unidad(es)")


def checkout(carro):
    total = 0

    for producto, cantidad in carro.items():
        if producto == '1' or producto == '2' or producto == '3':
            total += cantidad * 33.77
        elif producto == '4' or producto == '5':
            total += cantidad * 51.19

    if '1' in carro and '2' in carro and '3' in carro:
        total *= 0.8  # Aplicar descuento del 20% para los productos 1, 2 y 3
    elif '4' in carro and '5' in carro:
        total *= 0.85  # Aplicar descuento del 15% para los productos 4 y 5

    total = round(total, 1)  # Redondear el total a un decimal
    print(f"Total a pagar: USD {total}")


if __name__ == "__main__":
    carro = {}

    while True:
        orden = input("Ingrese la orden (agregar, ver, checkout): ")

        if orden == "agregar":
            producto, cantidad = input("Ingrese el producto y la cantidad: ").split(',')
            agregar_producto(carro, producto, int(cantidad))
        elif orden == "ver":
            mostrar_carro(carro)
        elif orden == "checkout":
            checkout(carro)
            break

      