# Diccionario de productos con su respectivo precio
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
def agregar_producto(producto, cantidad):
    if producto in carro:
        carro[producto] += cantidad
    else:
        carro[producto] = cantidad

# Función para mostrar los productos en el carro
def mostrar_carro():
    if len(carro) == 0:
        print("El carro está vacío.")
    else:
        print("Productos en el carro:")
        for producto, cantidad in carro.items():
            nombre = productos[producto]['nombre']
            precio_unitario = productos[producto]['precio']
            subtotal = precio_unitario * cantidad
            print(f"{cantidad} x {nombre} - Subtotal: USD {subtotal:.2f}")

# Función para calcular el total con descuentos y realizar el checkout
def checkout():
    total = 0
    for producto, cantidad in carro.items():
        precio_unitario = productos[producto]['precio']
