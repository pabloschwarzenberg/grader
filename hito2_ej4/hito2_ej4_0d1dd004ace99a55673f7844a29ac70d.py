# Diccionario de productos con sus precios
productos = {
    1: {'nombre': 'Juego Pokemon X para Nintendo 3DS', 'precio': 33.77},
    2: {'nombre': 'Nintendo 3DS XL', 'precio': 203},
    3: {'nombre': 'Juego Mario Kart 7 para Nintendo 3DS', 'precio': 27.58},
    4: {'nombre': 'PlayStation 4', 'precio': 348.00},
    5: {'nombre': 'FIFA 16, PlayStation 4', 'precio': 51.19}
}

# Carro de compras
carro = []

# Función para calcular el descuento
def calcular_descuento():
    total = sum(productos[producto]['precio'] for producto, _ in carro)
    if len(carro) >= 3 and all(producto in [1, 2, 3] for producto, _ in carro):
        return total * 0.8
    elif len(carro) >= 2 and all(producto in [4, 5] for producto, _ in carro):
        return total * 0.85
    else:
        return total

# Programa principal
while True:
    orden = input("Ingrese su orden (producto,cantidad / ver / checkout): ")
    if orden == "ver":
        print("Productos en el carro:")
        for producto, cantidad in carro:
            nombre = productos[producto]['nombre']
            precio = productos[producto]['precio']
            print(f"{nombre} x{cantidad} - Precio: {precio}")
    elif orden == "checkout":
        total_descuento = calcular_descuento()
        print(f"Total a pagar con descuento: {round(total_descuento, 1)}")
        break
    else:
        try:
            producto, cantidad = map(int, orden.split(","))
            if producto in productos and cantidad > 0:
                carro.append((producto, cantidad))
                print("Producto agregado al carro.")
            else:
                print("Ingrese un producto válido y una cantidad mayor a cero.")
        except ValueError:
            print("Orden inválida. Por favor, ingrese una orden válida.")
