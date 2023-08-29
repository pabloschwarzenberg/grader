# Diccionario de productos con sus precios
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

# Función para mostrar los productos en el carro
def mostrar_carro():
    for producto_id, cantidad in carro.items():
        producto = productos[producto_id]
        nombre = producto['nombre']
        precio_unitario = producto['precio']
        precio_total = precio_unitario * cantidad
        print(f'{nombre} - Cantidad: {cantidad} - Precio total: ${precio_total:.2f}')

# Función para calcular el descuento
def calcular_descuento():
    descuento = 0
    if set([1, 2, 3]).issubset(carro.keys()):
        descuento = 0.2
    elif set([4, 5]).issubset(carro.keys()):
        descuento = 0.15
    return descuento

# Función para calcular el precio total con descuento
def calcular_precio_total(descuento):
    precio_total = 0
    for producto_id, cantidad in carro.items():
        producto = productos[producto_id]
        precio_unitario = producto['precio']
        precio_total += precio_unitario * cantidad
    precio_total_con_descuento = precio_total - (precio_total * descuento)
    return round(precio_total_con_descuento, 1)

# Proceso principal del programa
while True:
    orden = input("Ingrese la orden (agregar, ver, checkout): ")
    
    if orden == "agregar":
        entrada = input("Ingrese el producto y la cantidad (ejemplo: 5,2): ")
        producto_id, cantidad = map(int, entrada.split(","))
        agregar_producto(producto_id, cantidad)
        print("Producto agregado al carro.")
    
    elif orden == "ver":
        mostrar_carro()
    
    elif orden == "checkout":
        descuento = calcular_descuento()
        precio_total_con_descuento = calcular_precio_total(descuento)
        print(f"Total a pagar: ${precio_total_con_descuento:.1f}")
        break
    
    else:
        print("Orden inválida. Intente nuevamente.")
