productos = {
    1: {'nombre': 'Juego Pokemon X para Nintendo 3DS', 'precio': 33.77},
    2: {'nombre': 'Nintendo 3DS XL', 'precio': 203.0},
    3: {'nombre': 'Juego Mario Kart 7 para Nintendo 3DS', 'precio': 27.58},
    4: {'nombre': 'PlayStation 4', 'precio': 348.0},
    5: {'nombre': 'FIFA 16, PlayStation 4', 'precio': 51.19}
}

carrito = {}
subtotal = 0.0

def calcular_total():
    total = subtotal
    if 1 in carrito and 2 in carrito and 3 in carrito:
        descuento = subtotal * 0.2
        total -= descuento
    elif 4 in carrito and 5 in carrito:
        descuento = subtotal * 0.15
        total -= descuento
    return round(total, 1)

while True:
    
    accion = input("Ingrese la acción (producto,cantidad / ver / checkout): ")

    
    if accion == 'ver':
        print("Productos en el carrito:")
        for producto, cantidad in carrito.items():
            nombre_producto = productos[producto]['nombre']
            print("{}x {}".format(cantidad, nombre_producto))
        print()
    elif accion == 'checkout':
        total = calcular_total()
        print("Total a pagar: USD {}".format(total))
        break
    else:
        
        try:
            producto, cantidad = map(int, accion.split(','))
            if producto in productos:
                if producto in carrito:
                    carrito[producto] += cantidad
                else:
                    carrito[producto] = cantidad
                subtotal += productos[producto]['precio'] * cantidad
                nombre_producto = productos[producto]['nombre']
                print("{}x {} agregado(s) al carrito.\n".format(cantidad, nombre_producto))
            else:
                print("Producto no válido.\n")
        except ValueError:
            print("Acción inválida.\n")

