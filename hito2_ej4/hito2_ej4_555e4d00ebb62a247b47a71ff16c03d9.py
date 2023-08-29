# Diccionario de productos
productos = {
    1: {'nombre': 'Juego Pokemon X para Nintendo 3DS', 'precio': 33.77},
    2: {'nombre': 'Nintendo 3DS XL', 'precio': 203},
    3: {'nombre': 'Juego Mario Kart 7 para Nintendo 3DS', 'precio': 27.58},
    4: {'nombre': 'PlayStation 4', 'precio': 348.00},
    5: {'nombre': 'FIFA 16, PlayStation 4', 'precio': 51.19}
}

# Carro de compras
carro = {}

# Función para agregar productos al carro
def agregar_producto(producto_id, cantidad):
    if producto_id in carro:
        carro[producto_id] += cantidad
    else:
        carro[producto_id] = cantidad

# Función para calcular el descuento y el precio total del carro
def calcular_precio_total():
    precio_total = 0

    # Descuento del 20% si se agregan los productos 1, 2 y 3 al carro
    if 1 in carro and 2 in carro and 3 in carro:
        precio_total += (productos[1]['precio'] + productos[2]['precio'] + productos[3]['precio']) * 0.8

    # Descuento del 15% si se agregan los productos 4 y 5 al carro
    elif 4 in carro and 5 in carro:
        precio_total += (productos[4]['precio'] + productos[5]['precio']) * 0.85

    # Precio sin descuento
    else:
        for producto_id, cantidad in carro.items():
            precio_total += productos[producto_id]['precio'] * cantidad

    return round(precio_total, 1)

# Solicitar acciones al usuario
while True:
    accion = input("Ingrese una acción (agregar, ver, checkout): ")

    if accion == "agregar":
        entrada = input("Ingrese el producto y la cantidad (producto,cantidad): ")
        producto_id, cantidad = map(int, entrada.split(','))

        if producto_id in productos:
            agregar_producto(producto_id, cantidad)
            print("Producto agregado al carro.")
        else:
            print("Producto no válido.")

    elif accion == "ver":
        print("Productos en el carro:")
        for producto_id, cantidad in carro.items():
            print(f"Producto {producto_id}: {productos[producto_id]['nombre']} - Cantidad: {cantidad}")

    elif accion == "checkout":
        precio_total = calcular_precio_total()
        print(f"Total a pagar: USD {precio_total}")
        break

    else:
        print("Acción inválida. Por favor, intente nuevamente.")
