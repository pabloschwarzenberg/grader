productos = {
    1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203},
    3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}

carrito = []

def agregar_producto(producto, cantidad):
    for i in range(cantidad):
        carrito.append(producto)

def calcular_total():
    total = sum(productos[producto]["precio"] for producto in carrito)

    if set([1, 2, 3]).issubset(carrito):
        total *= 0.8  # Aplica descuento del 20% si se agregan productos 1, 2 y 3
    elif set([4, 5]).issubset(carrito):
        total *= 0.85  # Aplica descuento del 15% si se agregan productos 4 y 5

    return round(total, 1)

if __name__ == "__main__":
    while True:
        orden = input("Ingrese la orden (producto,cantidad / ver / checkout): ")

        if orden == "ver":
            print("Productos en el carrito:")
            for producto in carrito:
                print(f"- {productos[producto]['nombre']}")
        elif orden == "checkout":
            total = calcular_total()
            print(f"Total a pagar: USD {total}")
            break
        else:
            try:
                producto, cantidad = orden.split(",")
                producto = int(producto)
                cantidad = int(cantidad)

                if producto in productos:
                    agregar_producto(producto, cantidad)
                    print(f"Se agregaron {cantidad} unidad(es) del producto {producto} al carrito.")
                else:
                    print("Producto no válido.")
            except ValueError:
                print("Orden no válida.")
