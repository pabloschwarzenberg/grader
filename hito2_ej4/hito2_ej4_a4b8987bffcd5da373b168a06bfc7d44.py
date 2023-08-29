productos = {
    1: ("Juego Pokemon X para Nintendo 3DS", 33.77),
    2: ("Nintendo 3DS XL", 203),
    3: ("Juego Mario Kart 7 para Nintendo 3DS", 27.58),
    4: ("PlayStation 4", 348.00),
    5: ("FIFA 16, PlayStation 4", 51.19)
}

carro = {}

while True:
    comando = input("Ingresa un comando: ")
    if comando == "ver":
        for producto, cantidad in carro.items():
            nombre, precio = productos[producto]
            print(nombre":", cantidad "x USD", precio:.2f)
    elif comando == "checkout":
        total = 0
        descuento = 0
        for producto, cantidad in carro.items():
            nombre, precio = productos[producto]
            total += precio * cantidad
            if producto in [1, 2, 3]:
                descuento += precio * cantidad * 0.2
            elif producto in [4, 5]:
                descuento += precio * cantidad * 0.15
        total -= descuento
        print(f"Total: USD {total:.1f}")
        break
    else:
        producto, cantidad = map(int, comando.split(","))
        if producto in carro:
            carro[producto] += cantidad
        else:
            carro[producto] = cantidad
