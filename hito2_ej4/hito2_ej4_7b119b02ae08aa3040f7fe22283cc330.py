productos = {
    1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203.00},
    3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}

carrito = {}
subtotal = 0.0

while True:
    orden = input("Ingrese su orden (producto,cantidad / ver / checkout): ")

    if orden == "checkout":
        if len(carrito) == 0:
            print("El carrito está vacío.")
        else:
            total = subtotal
            if 1 in carrito and 2 in carrito and 3 in carrito:
                descuento = subtotal * 0.2
                total -= descuento
            elif 4 in carrito and 5 in carrito:
                descuento = subtotal * 0.15
                total -= descuento

            print("Checkout:")
            for producto_id, cantidad in carrito.items():
                producto = productos[producto_id]
                nombre = producto["nombre"]
                precio = producto["precio"]
                subtotal_producto = precio * cantidad
                print(f"{nombre} (Cantidad: {cantidad}) - Subtotal: ${subtotal_producto:.1f}")

            print("Total a pagar: $", round(total, 1))
            break

    elif orden == "ver":
        if len(carrito) == 0:
            print("El carrito está vacío.")
        else:
            print("Productos en el carrito:")
            for producto_id, cantidad in carrito.items():
                producto = productos[producto_id]
                nombre = producto["nombre"]
                precio = producto["precio"]
                print(f"{nombre} (Cantidad: {cantidad}) - Precio unitario: ${precio:.2f}")

    else:
        orden_split = orden.split(",")
        producto_id = int(orden_split[0])
        cantidad = int(orden_split[1])

        if producto_id in productos:
            if producto_id in carrito:
                carrito[producto_id] += cantidad
            else:
                carrito[producto_id] = cantidad

            precio = productos[producto_id]["precio"]
            subtotal += precio * cantidad

        else:
            print("Producto no válido.")
