productos = {
    '1': {'nombre': 'Juego Pokemon X para Nintendo 3DS', 'precio': 33.77},
    '2': {'nombre': 'Nintendo 3DS XL', 'precio': 203},
    '3': {'nombre': 'Juego Mario Kart 7 para Nintendo 3DS', 'precio': 27.58},
    '4': {'nombre': 'PlayStation 4', 'precio': 348.00},
    '5': {'nombre': 'FIFA 16, PlayStation 4', 'precio': 51.19}
}

carro = {}
descuento = 0

while True:
    orden = input("Ingrese una orden ('producto,cantidad', 'ver', 'checkout'): ")

    if orden == 'checkout':
        total = sum([productos[producto]['precio'] * cantidad for producto, cantidad in carro.items()])
        if descuento != 0:
            total -= total * descuento
        print("Total a pagar: {:.1f}".format(total))
        break

    elif orden == 'ver':
        print("Productos en el carro:")
        for producto, cantidad in carro.items():
            nombre = productos[producto]['nombre']
            precio = productos[producto]['precio']
            print("Producto: {}, Cantidad: {}, Precio unitario: {:.2f}".format(nombre, cantidad, precio))

    else:
        producto, cantidad = orden.split(',')
        if producto in productos:
            if producto in carro:
                carro[producto] += int(cantidad)
            else:
                carro[producto] = int(cantidad)

            # Aplicar descuentos
            if len(carro) == 3 and {'1', '2', '3'}.issubset(carro.keys()):
                descuento = 0.2
            elif {'4', '5'}.issubset(carro.keys()):
                descuento = 0.15
            else:
                descuento = 0

            print("Producto agregado al carro.")

        else:
            print("Producto inválido.")
