# Diccionario de productos con su información
productos = {
    1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203},
    3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}

# Carrito de compras
carrito = []

def agregar_producto(producto, cantidad):
    carrito.append((producto, cantidad))

def imprimir_productos():
    for item in carrito:
        producto = productos[item[0]]
        nombre = producto["nombre"]
        precio = producto["precio"]
        cantidad = item[1]
        print(f"Producto: {nombre} - Cantidad: {cantidad} - Precio unitario: ${precio}")

def hacer_checkout():
    descuento = 0
    for item in carrito:
        producto = productos[item[0]]
        precio = producto["precio"]
        cantidad = item[1]
        subtotal = precio * cantidad
        if item[0] in [1, 2, 3] and len(carrito) >= 3:
            # Aplicar descuento del 20% si se agregaron los productos 1, 2 y 3 al carro
            descuento += subtotal * 0.2
        elif item[0] in [4, 5] and len(carrito) >= 2:
            # Aplicar descuento del 15% si se agregaron los productos 4 y 5 al carro
            descuento += subtotal * 0.15

    total = sum([producto["precio"] * cantidad for producto, cantidad in carrito])
    total -= descuento

    print(f"Total a pagar: ${round(total, 1)}")

# Loop principal
while True:
    accion = input("Ingrese 'agregar', 'ver' o 'checkout': ")
    
    if accion == "agregar":
        entrada = input("Ingrese el producto y la cantidad en el formato 'producto,cantidad': ")
        producto, cantidad = map(int, entrada.split(","))
        if producto in productos.keys() and cantidad > 0:
            agregar_producto(producto, cantidad)
        else:
            print("Producto o cantidad inválidos. Intente nuevamente.")
    elif accion == "ver":
        imprimir_productos()
    elif accion == "checkout":
        hacer_checkout()
        break
    else:
        print("Acción no válida. Intente nuevamente.")
