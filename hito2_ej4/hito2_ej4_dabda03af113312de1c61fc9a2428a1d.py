# Definir los productos y sus precios
productos = {
    1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203},
    3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}

# Inicializar el carrito de compras
carrito = []

# Función para agregar productos al carrito
def agregar_producto(producto, cantidad):
    producto_id = int(producto)
    carrito.append((producto_id, cantidad))

# Función para mostrar los productos en el carrito
def ver_carrito():
    for producto_id, cantidad in carrito:
        producto = productos[producto_id]
        print(f"{producto['nombre']} - Cantidad: {cantidad}")

# Función para calcular el precio total con descuentos
def calcular_total():
    descuento = 0
    
    # Verificar si se aplican descuentos
    descuento_20 = all(producto_id in [1, 2, 3] for producto_id, _ in carrito)
    descuento_15 = all(producto_id in [4, 5] for producto_id, _ in carrito)
    
    if descuento_20:
        descuento = 0.2
    elif descuento_15:
        descuento = 0.15
    
    total = 0
    for producto_id, cantidad in carrito:
        producto = productos[producto_id]
        total += producto['precio'] * cantidad
    
    total_descuento = total - (total * descuento)
    return round(total_descuento, 1)

# Obtener las órdenes del usuario
while True:
    orden = input("Ingrese una orden (producto,cantidad / ver / checkout): ")
    
    if orden == "ver":
        ver_carrito()
    elif orden == "checkout":
        total_descuento = calcular_total()
        print(f"Total a pagar: USD {total_descuento}")
        break
    else:
        producto, cantidad = orden.split(",")
        agregar_producto(producto, int(cantidad))
