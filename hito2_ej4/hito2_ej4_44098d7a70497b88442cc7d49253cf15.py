def agregar_producto(carro, producto, cantidad):
    carro[producto] = carro.get(producto, 0) + cantidad

def mostrar_productos(carro):
    for producto, cantidad in carro.items():
        print("Producto {}: {} unidades".format(producto, cantidad))

def checkout(carro):
    total = 0
    descuento = 0

    p1 = [1, "Pokemon X", 33.77]
    p2 = [2, "Nintendo XL", 203]
    p3 = [3, "Mario Kart 7", 27.58]
    p4 = [4, "PlayStation 4", 348.00]
    p5 = [5, "FIFA 16", 51.19]

    for producto, cantidad in carro.items():
        if producto == 1:
            total += cantidad * p1[2]
        elif producto == 2:
            total += cantidad * p2[2]
        elif producto == 3:
            total += cantidad * p3[2]
        elif producto == 4:
            total += cantidad * p4[2]
        elif producto == 5:
            total += cantidad * p5[2]
    
    if 1 in carro and 2 in carro and 3 in carro:
        descuento = total * 0.2
    elif 4 in carro and 5 in carro:
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