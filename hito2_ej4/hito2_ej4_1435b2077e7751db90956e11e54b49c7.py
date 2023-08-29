productos = {
    1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203},
    3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}

carrito = {}
descuentos = {
    frozenset({1, 2, 3}): 0.2,  # Descuento del 20% si se agregan los productos 1, 2 y 3 al carro
    frozenset({4, 5}): 0.15    # Descuento del 15% si se agregan los productos 4 y 5 al carro
}

def agregar_producto(producto, cantidad):
    producto_id = int(producto)
    if producto_id not in productos:
        print("Producto no válido")
        return

    if producto_id in carrito:
        carrito[producto_id] += cantidad
    else:
        carrito[producto_id] = cantidad

    print(f"Se han agregado {cantidad} unidad(es) del producto {producto_id} al carrito")

def mostrar_productos():
    for producto_id, producto_info in productos.items():
        print(f"{producto_id}: {producto_info['nombre']}, USD {producto_info['precio']}")

def calcular_descuento():
    descuento = 0.0
    for productos_descuento, porcentaje_descuento in descuentos.items():
        if all(producto in carrito for producto in productos_descuento):
            descuento = porcentaje_descuento
            break

    total = sum(productos["precio"] * cantidad for producto, cantidad in carrito.items())
    total_descuento = total * (1 - descuento)
    return round(total_descuento, 1)

while True:
    opcion = input("Ingresa una opción (producto,cantidad / ver / checkout / salir): ")

    if opcion == "salir":
        break
    elif opcion == "ver":
        mostrar_productos()
    elif opcion == "checkout":
        total_descuento = calcular_descuento()
        print(f"Total a pagar (con descuento): USD {total_descuento}")
        carrito = {}
    else:
        try:
            producto, cantidad = opcion.split(",")
            agregar_producto(producto, int(cantidad))
        except ValueError:
            print("Entrada inválida")
