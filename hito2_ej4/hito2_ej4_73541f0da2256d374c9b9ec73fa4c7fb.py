p1 = [1, "Pokemon X", 33.77]
p2 = [2, "Nintendo XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16", 51.19]

carrito = []

def agregar_producto(producto_cantidad):
    producto_cantidad = producto_cantidad.split(",")
    if len(producto_cantidad) != 2:
        print("Formato de producto y cantidad inválido. Intente nuevamente.")
        return

    producto = producto_cantidad[0]
    cantidad = producto_cantidad[1]

    if not producto.isdigit() or not cantidad.isdigit():
        print("Formato de producto y cantidad inválido. Intente nuevamente.")
        return

    producto_id = int(producto)
    cantidad = int(cantidad)

    if producto_id >= 1 and producto_id <= 5:
        carrito.append((producto_id, cantidad))
        print("Producto agregado al carrito.")
    else:
        print("El producto no es válido.")

def ver_carrito():
    if len(carrito) == 0:
        print("El carrito está vacío.")
    else:
        print("Productos en el carrito:")
        for producto_id, cantidad in carrito:
            nombre_producto = ""
            if producto_id == 1:
                nombre_producto = p1[1]
            elif producto_id == 2:
                nombre_producto = p2[1]
            elif producto_id == 3:
                nombre_producto = p3[1]
            elif producto_id == 4:
                nombre_producto = p4[1]
            elif producto_id == 5:
                nombre_producto = p5[1]
            print("Producto: {}, Cantidad: {}".format(nombre_producto, cantidad))

def calcular_total():
    total = 0
    descuento = 0
    productos_descuento = {1, 2, 3}
    productos_descuento2 = {4, 5}

    for producto_id, cantidad in carrito:
        if producto_id in productos_descuento:
            total += globals()["p{}".format(producto_id)][2] * cantidad
        elif producto_id in productos_descuento2:
            total += globals()["p{}".format(producto_id)][2] * cantidad

    if all(item in [producto_id for producto_id, _ in carrito] for item in productos_descuento):
        descuento = total * 0.2
    elif all(item in [producto_id for producto_id, _ in carrito] for item in productos_descuento2):
        descuento = total * 0.15

    total -= descuento
    total = round(total, 2)

    return total

while True:
    orden = input("Ingrese el número de producto y la cantidad separados por coma, o la opción 'ver' o 'checkout': ")
    orden = orden.lower()

    if orden == "ver":
        ver_carrito()
    elif orden == "checkout":
        total = calcular_total()
        print(total)
        break
    else:
        agregar_producto(orden)
