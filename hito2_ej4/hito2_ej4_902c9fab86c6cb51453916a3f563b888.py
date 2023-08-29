productos = {
    1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203},
    3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}

carro_compras = {}

def agregar_producto(producto_id, cantidad):
    if producto_id in productos:
        if producto_id in carro_compras:
            carro_compras[producto_id] += cantidad
        else:
            carro_compras[producto_id] = cantidad
        print(f"Se agregaron {cantidad} unidad(es) del producto {producto_id} al carro.")
    else:
        print(f"El producto {producto_id} no existe.")

def ver_productos():
    for producto_id, cantidad in carro_compras.items():
        producto = productos[producto_id]
        nombre = producto["nombre"]
        precio_unitario = producto["precio"]
        precio_total = precio_unitario * cantidad
        print(f"Producto: {nombre} - Cantidad: {cantidad} - Precio total: ${precio_total:.2f}")

def checkout():
    descuento = 0

    if 1 in carro_compras and 2 in carro_compras and 3 in carro_compras:
        descuento = 0.2
    elif 4 in carro_compras and 5 in carro_compras:
        descuento = 0.15

    total = 0
    for producto_id, cantidad in carro_compras.items():
        producto = productos[producto_id]
        precio_unitario = producto["precio"]
        total += precio_unitario * cantidad

    total_descuento = total - (total * descuento)
    print(f"Total a pagar (con descuento): ${total_descuento:.1f}")

while True:
    accion = input("¿Qué deseas hacer? (agregar, ver, checkout, salir): ")

    if accion == "salir":
        break
    elif accion == "agregar":
        entrada = input("Ingrese el producto y la cantidad en el formato producto,cantidad: ")
        producto_id, cantidad = map(int, entrada.split(","))
        agregar_producto(producto_id, cantidad)
    elif accion == "ver":
        ver_productos()
    elif accion == "checkout":
        checkout()
    else:
        print("Acción inválida. Por favor, intenta nuevamente.")