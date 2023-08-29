productos = {
    1: {"nombre": "juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "nintendo 3DS XL", "precio": 203},
    3: {"nombre": "juego Mario Kart 7 nintendo 3DS", "precio": 27.58},
    4: {"nombre": "playStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}
carro = []
while True:
    entrada = input("ingrese un producto, 'ver' para ver los productos en el carro o 'checkout' para finalizar la compra: ")
    if entrada == "ver":
        print("productos en carro:")
        for producto in carro:
            print("- {} (cantidad: {})".format(productos[producto[0]]["nombre"], producto[1]))
    elif entrada == "checkout":
        subtotal = 0
        descuento = 0
        for producto in carro:
            subtotal += productos[producto[0]]["precio"] * producto[1]
        if (1 in [p[0] for p in carro]) and (2 in [p[0] for p in carro]) and (3 in [p[0] for p in carro]):
            descuento = subtotal * 0.2
        elif (4 in [p[0] for p in carro]) and (5 in [p[0] for p in carro]):
            descuento = subtotal * 0.15
        total = subtotal - descuento
        print("Total: USD {:.1f}".format(total))
        break
    else:
        producto, cantidad = map(int, entrada.split(","))
        if producto not in productos:
            print("producto no encontrado.")
        else:
            carro.append((producto, cantidad))
            print("se agregó al carro: {} (cantidad: {})".format(productos[producto]["nombre"], cantidad))

