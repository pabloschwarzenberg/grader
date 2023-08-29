def agregar_producto(carro, producto, cantidad):
    if producto in carro:
        carro[producto] += cantidad
    else:
        carro[producto] = cantidad

def imprimir_carro(carro, productos):
    for producto, cantidad in carro.items():
        nombre = productos[producto][1]
        precio_unitario = productos[producto][2]
        precio_total = precio_unitario * cantidad
        print(nombre, cantidad, precio_total)

def hacer_checkout(carro, productos):
    total = 0

    for producto, cantidad in carro.items():
        precio_unitario = productos[producto][2]
        total += precio_unitario * cantidad

    if len(carro) >= 3 and set(carro.keys()).issuperset({1, 2, 3}):
        total *= 0.8
    elif len(carro) >= 2 and set(carro.keys()).issuperset({4, 5}):
        total *= 0.85

    print(total)

if __name__ == "__main__":
    productos = {
        1: [1, "Pokemon X para Nintendo 3DS", 33.77],
        2: [2, "Nintendo 3DS XL", 203],
        3: [3, "Mario Kart 7 para Nintendo 3DS", 27.58],
        4: [4, "PlayStation 4", 348.00],
        5: [5, "FIFA 16, PlayStation 4", 51.19]
    }

    carro = {}

    while True:
        accion = input("Ingrese una acción (agregar, ver, checkout): ")

        if accion == "agregar":
            entrada = input("Ingrese el producto y cantidad (producto,cantidad): ")
            producto, cantidad = map(int, entrada.split(","))
            agregar_producto(carro, producto, cantidad)
        elif accion == "ver":
            imprimir_carro(carro, productos)
        elif accion == "checkout":
            hacer_checkout(carro, productos)
            break
        else:
            print("Acción no válida. Intente nuevamente.")