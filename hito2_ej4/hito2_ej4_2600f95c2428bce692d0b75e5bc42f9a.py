def agregar_producto(carrito, producto, cantidad):
    if producto in carrito:
        carrito[producto] += cantidad
    else:
        carrito[producto] = cantidad

def imprimir_carrito(carrito, precios):
    print("Carrito de compras:")
    for producto, cantidad in carrito.items():
        precio_unitario = precios[producto]
        subtotal = precio_unitario * cantidad
        print("Producto {producto}: {cantidad} unidad(es) - Subtotal: USD {subtotal:.2f}")

def checkout(carrito, precios):
    total = 0

    for producto, cantidad in carrito.items():
        precio_unitario = precios[producto]
        subtotal = precio_unitario * cantidad
        total += subtotal

    # Aplicar descuentos
    if '1' in carrito and '2' in carrito and '3' in carrito:
        descuento = total * 0.2
        total -= descuento
    elif '4' in carrito and '5' in carrito:
        descuento = total * 0.15
        total -= descuento

    total = round(total, 1)
    print("Total a pagar: USD {total:.1f}")

# Precios de los productos
precios = {
    '1': 33.77,
    '2': 203.0,
    '3': 27.58,
    '4': 348.0,
    '5': 51.19
}

# Carrito de compras
carrito = {}

while True:
    accion = input("¿Qué desea hacer? (agregar, ver, checkout, salir): ")

    if accion == "agregar":
        producto, cantidad = input("Ingrese el producto y cantidad: ").split(",")
        agregar_producto(carrito, producto, int(cantidad))
    elif accion == "ver":
        imprimir_carrito(carrito, precios)
    elif accion == "checkout":
        checkout(carrito, precios)
        break
    elif accion == "salir":
        break
    else:
        print("Acción no válida. Por favor, intente nuevamente.")

