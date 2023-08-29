def agregar_producto(carro, producto, cantidad):
    carro[producto] = carro.get(producto, 0) + cantidad

def mostrar_productos(carro):
    for producto, cantidad in carro.items():
        print("Producto {}: {} unidades".format(producto, cantidad))

def checkout(carro):
    total = 0
    descuento = 0

    productos = {
        1: ["Pokemon X", 33.77],
        2: ["Nintendo XL", 203],
        3: ["Mario Kart 7", 27.58],
        4: ["PlayStation 4", 348.00],
        5: ["FIFA 16", 51.19]
    }

    for producto, cantidad in carro.items():
        if producto in productos:
            total += cantidad * productos[producto][1]

    if set([1, 2, 3]).issubset(carro.keys()):
        descuento = total * 0.2
    elif set([4, 5]).issubset(carro.keys()):
        descuento = total * 0.15

    total -= descuento

    print("Total a pagar: {} USD".format(round(total, 1)))

carro = {}

while True:
    orden = input("Ingresa una orden (producto,cantidad / ver / checkout): ")

    if orden == "ver":
        mostrar_productos(carro)
    elif orden == "checkout":
        checkout(carro)
        break
    else:
        try:
            producto, cantidad = map(int, orden.split(","))
            agregar_producto(carro, producto, cantidad)
        except ValueError:
            print("Orden inválida. Inténtalo nuevamente.")
