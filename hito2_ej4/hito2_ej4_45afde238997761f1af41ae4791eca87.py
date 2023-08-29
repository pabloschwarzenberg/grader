productos = {
    1: ("Juego Pokemon X para Nintendo 3DS", 33.77),
    2: ("Nintendo 3DS XL", 203),
    3: ("Juego Mario Kart 7 para Nintendo 3DS", 27.58),
    4: ("PlayStation 4", 348.00),
    5: ("FIFA 16, PlayStation 4", 51.19)
}

carro = {}

while True:
    orden = input().strip()

    if orden == "checkout":
        total = sum(precio * cantidad for (producto, cantidad), (nombre, precio) in carro.items())
        descuento = total * 0.2 if all(producto in carro for producto in [(1, 1), (2, 1), (3, 1)]) else total * 0.15 if all(producto in carro for producto in [(4, 1), (5, 1)]) else 0
        total -= descuento
        print(round(total, 1))
        break

    elif orden == "ver":
        for (producto, cantidad), (nombre, precio) in carro.items():
            print(f"Producto {producto}: {nombre} - USD {precio}")

    else:
        try:
            producto, cantidad = map(int, orden.split(","))
            if producto in productos:
                carro[(producto, cantidad)] = productos[producto]
        except ValueError:
            pass


