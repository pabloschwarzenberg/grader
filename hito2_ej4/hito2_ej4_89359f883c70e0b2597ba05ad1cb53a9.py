productos = {
    1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203},
    3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}

carro = []

def agregar_producto(producto, cantidad):
    for i in range(cantidad):
        carro.append(producto)

def mostrar_productos():
    for producto in carro:
        print(f"Producto: {productos[producto]['nombre']}")

def calcular_total():
    total = 0
    descuento = 0

    if set([1, 2, 3]).issubset(carro):
        descuento = 0.2
    elif set([4, 5]).issubset(carro):
        descuento = 0.15

    for producto in carro:
        total += productos[producto]['precio']

    total -= total * descuento

    return round(total, 1)


while True:
    orden = input("Ingrese una orden (agregar, ver, checkout): ")

    if orden == "agregar":
        entrada = input("Ingrese el producto y cantidad: ")
        producto, cantidad = map(int, entrada.split(","))
        agregar_producto(producto, cantidad)
    elif orden == "ver":
        mostrar_productos()
    elif orden == "checkout":
        total = calcular_total()
        print(f"Total a pagar: USD {total}")
        break
