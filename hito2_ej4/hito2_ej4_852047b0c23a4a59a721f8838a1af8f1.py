productos = [
    ["Juego Pokemon X para Nintendo 3DS", 33.77],
    ["Nintendo 3DS XL", 203],
    ["Juego Mario Kart 7 para Nintendo 3DS", 27.58],
    ["PlayStation 4", 348.00],
    ["FIFA 16, PlayStation 4", 51.19]
]

carro = []
subtotal1 = 0.0
subtotal2 = 0.0


def agregar_producto(producto_id, cantidad):
    global subtotal1
    global subtotal2
    if producto_id >= 1 and producto_id <= len(productos):
        producto = productos[producto_id - 1]
        precio = producto[1] * cantidad
        carro.append((producto[0], cantidad, precio))
        if producto_id in [1,2,3]:
            subtotal1 += precio
        else:
            subtotal2 += precio
        print('Se agregaron', cantidad, 'unidades del producto', producto_id, 'al carro')


def mostrar_productos():
    if len(carro) > 0:
        print("Productos en el carro:")
        for producto in carro:
            print("Producto:", producto[0], ", Cantidad:", producto[1], ", Precio:", producto[2])
    else:
        print("El carro está vacío.")


def aplicar_descuento():
    global subtotal1
    global subtotal2
    descuento1 = 0.0
    descuento2 = 0.0

    # Verificar si se aplican descuentos
    productos_agregados = [producto_id for producto_id, _, _ in carro]
    if len(carro) >= 3 and all(producto_id in [1, 2, 3] for producto_id in productos_agregados):
        descuento1 = subtotal1 * 0.2
    elif len(carro) >= 2 and all(producto_id in [4, 5] for producto_id in productos_agregados):
        descuento2 = subtotal2 * 0.15

    total = subtotal1 + subtotal2 - descuento1 - descuento2
    print("Total a pagar (con descuento):", round(total, 1))


def procesar_orden(orden):
    if orden == "ver":
        mostrar_productos()
    elif orden == "checkout":
        aplicar_descuento()
    else:
        try:
            producto_id, cantidad = map(int, orden.split(","))
            agregar_producto(producto_id, cantidad)
        except ValueError:
            print("Orden inválida.")


entrada = 0
while entrada != 'checkout':
    entrada = input("Ingrese una orden (producto,cantidad / ver / checkout): ")
    procesar_orden(entrada)