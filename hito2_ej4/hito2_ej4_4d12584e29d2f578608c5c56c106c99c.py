# Definimos los productos y sus precios
productos = {
    1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203},
    3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}

# Definimos los descuentos
descuentos = {
    frozenset([1, 2, 3]): 0.2,
    frozenset([4, 5]): 0.15
}

# Inicializamos el carrito de compras
carrito = {}

# Función para agregar productos al carrito
def agregar_producto(producto, cantidad):
    producto_id = int(producto)
    if producto_id not in productos:
        print("Producto inválido")
        return
    if producto_id in carrito:
        carrito[producto_id] += int(cantidad)
    else:
        carrito[producto_id] = int(cantidad)
    print(f"Se agregaron {cantidad} unidades del producto {producto_id}")

# Función para mostrar los productos en el carrito
def ver_carrito():
    total = 0
    for producto_id, cantidad in carrito.items():
        producto = productos[producto_id]
        subtotal = cantidad * producto["precio"]
        print(f"{producto['nombre']} x {cantidad}: ${subtotal:.2f}")
        total += subtotal
    print(f"Total: ${total:.2f}")

# Función para aplicar descuentos
def aplicar_descuentos():
    grupos_descuento = {}
    for producto_id, cantidad in carrito.items():
        for grupo, descuento in descuentos.items():
            if producto_id in grupo:
                if grupo not in grupos_descuento:
                    grupos_descuento[grupo] = 0
                grupos_descuento[grupo] += cantidad * productos[producto_id]["precio"]
    descuento_total = 0
    for grupo, subtotal in grupos_descuento.items():
        descuento = subtotal * descuentos[grupo]
        print(f"Descuento del {descuentos[grupo]*100:.0f}% por comprar {', '.join([str(p) for p in grupo])}: ${descuento:.2f}")
        descuento_total += descuento
    return descuento_total

# Función para hacer el checkout
def checkout():
    ver_carrito()
    descuento_total = aplicar_descuentos()
    total = sum([cantidad * producto["precio"] for producto_id, cantidad in carrito.items()])
    total -= descuento_total
    print(f"Total a pagar: ${total:.2f}")

# Loop principal
while True:
    accion = input("¿Qué desea hacer? (agregar, ver, checkout): ")
    if accion == "agregar":
        producto, cantidad = input("Ingrese el producto y la cantidad (en formato 'producto,cantidad'): ").split(",")
        agregar_producto(producto, cantidad)
    elif accion == "ver":
        ver_carrito()
    elif accion == "checkout":
        checkout()
        break
    else:
        print("Acción inválida")