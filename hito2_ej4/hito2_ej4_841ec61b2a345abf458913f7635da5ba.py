
# Diccionario de productos con sus respectivos precios
productos = {
    1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203},
    3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}

# Diccionario de descuentos
descuentos = {
    frozenset([1, 2, 3]): 0.2,   # Descuento del 20% si se agregan los productos 1, 2 y 3
    frozenset([4, 5]): 0.15      # Descuento del 15% si se agregan los productos 4 y 5
}

carro = {}  # Diccionario para almacenar los productos agregados al carro

def agregar_producto(producto, cantidad):
    producto = int(producto)
    cantidad = int(cantidad)
    if producto in productos:
        if producto in carro:
            carro[producto] += cantidad
        else:
            carro[producto] = cantidad
        print(f"Se agregaron {cantidad} unidad(es) del producto {producto} al carro.")
    else:
        print(f"No existe el producto {producto}.")

def mostrar_carro():
    if carro:
        print("Productos en el carro:")
        total_precio = 0
        for producto, cantidad in carro.items():
            nombre = productos[producto]["nombre"]
            precio = productos[producto]["precio"]
            subtotal = precio * cantidad
            total_precio += subtotal
            print(f"{cantidad} unidad(es) de {nombre} - Subtotal: ${subtotal:.2f}")
        print(f"Total: ${total_precio:.2f}")
    else:
        print("El carro está vacío.")

def checkout():
    total_precio = 0
    for producto, cantidad in carro.items():
        precio = productos[producto]["precio"]
        subtotal = precio * cantidad
        total_precio += subtotal

    # Aplicar descuentos si corresponde
    for productos_descuento, porcentaje_descuento in descuentos.items():
        if productos_descuento.issubset(carro.keys()):
            descuento = total_precio * porcentaje_descuento
            total_precio -= descuento

    print(f"Total a pagar (con descuento): ${total_precio:.1f}")

# Ejemplo de uso
agregar_producto("1", "2")   # Agregar 2 unidades del producto 1
agregar_producto("2", "1")   # Agregar 1 unidad del producto 2
agregar_producto("3", "3")   # Agregar 3 unidades del producto 3
mostrar_carro()              # Mostrar los productos en el carro
checkout()                   # Realizar el checkout


