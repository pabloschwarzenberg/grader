# Diccionario de productos
productos = {
    '1': {'nombre': 'Juego Pokemon X para Nintendo 3DS', 'precio': 33.77},
    '2': {'nombre': 'Nintendo 3DS XL', 'precio': 203.0},
    '3': {'nombre': 'Juego Mario Kart 7 para Nintendo 3DS', 'precio': 27.58},
    '4': {'nombre': 'PlayStation 4', 'precio': 348.0},
    '5': {'nombre': 'FIFA 16, PlayStation 4', 'precio': 51.19}
}

# Carro de compras
carro = {}

def agregar_producto(producto_id, cantidad):
    if producto_id in productos:
        if producto_id in carro:
            carro[producto_id] += cantidad
        else:
            carro[producto_id] = cantidad
        print(f"Producto agregado al carro: {productos[producto_id]['nombre']} - Cantidad: {cantidad}")
    else:
        print("Producto no válido.")

def mostrar_productos():
    if carro:
        print("Productos en el carro:")
        for producto_id, cantidad in carro.items():
            producto = productos[producto_id]
            nombre = producto['nombre']
            precio = producto['precio']
            subtotal_producto = precio * cantidad
            print(f"Producto: {nombre} - Cantidad: {cantidad} - Precio subtotal: {subtotal_producto:.2f}")
    else:
        print("El carro está vacío.")

def checkout():
    subtotal = 0.0
    descuento = 0.0

    for producto_id, cantidad in carro.items():
        producto = productos[producto_id]
        precio = producto['precio']
        subtotal_producto = precio * cantidad
        subtotal += subtotal_producto

    if '1' in carro and '2' in carro and '3' in carro:
        descuento = subtotal * 0.2
    elif '4' in carro and '5' in carro:
        descuento = subtotal * 0.15

    total = subtotal - descuento
    total = round(total, 1)

    print(f"Subtotal: {subtotal:.1f}")
    print(f"Descuento: {descuento:.1f}")
    print(f"Total: {total:.1f}")

# Programa principal
while True:
    orden = input("Ingrese una orden ('agregar', 'ver', 'checkout', 'salir'): ")

    if orden == 'agregar':
        datos = input("Ingrese el producto y la cantidad en el formato producto,cantidad: ")
        producto_id, cantidad = datos.split(',')
        agregar_producto(producto_id, int(cantidad))
    elif orden == 'ver':
        mostrar_productos()
    elif orden == 'checkout':
        checkout()
        break
    elif orden == 'salir':
        break
    else:
        print("Orden no válida.")

