def agregar_producto(carro, producto_id, cantidad):
    # Verificar si el producto ya está en el carro
    for producto in carro:
        if producto[0] == producto_id:
            producto[1] += cantidad
            return

    # Si el producto no está en el carro, agregarlo
    if producto_id == 1:
        producto = [1, "Pokemon X", 33.77]
    elif producto_id == 2:
        producto = [2, "Nintendo 3DS XL", 203]
    elif producto_id == 3:
        producto = [3, "Mario Kart 7", 27.58]
    elif producto_id == 4:
        producto = [4, "PlayStation 4", 348.00]
    elif producto_id == 5:
        producto = [5, "FIFA 16, PlayStation 4", 51.19]
    else:
        print("Producto no válido")
        return

    producto[1] = cantidad
    carro.append(producto)


def ver_productos(carro):
    print("Productos en el carro:")
    for producto in carro:
        print(f"{producto[0]}: {producto[1]} unidad(es) - {producto[2]} USD")


def hacer_checkout(carro):
    total = 0

    for producto in carro:
        total += producto[1] * producto[2]

    if len(carro) >= 3 and all(producto[0] in [1, 2, 3] for producto in carro):
        total *= 0.8  # Aplicar descuento del 20% para productos 1, 2 y 3
    elif len(carro) >= 2 and all(producto[0] in [4, 5] for producto in carro):
        total *= 0.85  # Aplicar descuento del 15% para productos 4 y 5

    total = round(total, 1)
    print("Total a pagar:", total, "USD")


if __name__ == "__main__":
    carro = []

    while True:
        orden = input("Ingrese una orden (producto,cantidad / ver / checkout): ")

        if orden == "ver":
            ver_productos(carro)
        elif orden == "checkout":
            hacer_checkout(carro)
            break
        else:
            try:
                producto_id, cantidad = map(int, orden.split(","))
                agregar_producto(carro, producto_id, cantidad)
            except ValueError:
                print("Orden no válida")

      