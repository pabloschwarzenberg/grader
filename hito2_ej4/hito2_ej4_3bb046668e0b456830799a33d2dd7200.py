p1 = [1, "Pokemon X", 33.77]
p2 = [2, "Nintendo XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16", 51.19]

carrito = {}

def agregar_al_carrito(producto, cantidad):
    if producto not in carrito:
        carrito[producto] = cantidad
    else:
        carrito[producto] += cantidad

def mostrar_carrito():
    print("Productos en el carrito:")
    for producto, cantidad in carrito.items():
        print(f"Cantidad: {cantidad} - Producto: {producto[1]}")

def calcular_total():
    total = 0
    descuento = 0

    for producto, cantidad in carrito.items():
        if producto == p1[0] or producto == p2[0] or producto == p3[0]:
            total += cantidad * producto[2]
            descuento = 0.2
        elif producto == p4[0] or producto == p5[0]:
            total += cantidad * producto[2]
            descuento = 0.15

    total -= total * descuento
    return round(total, 2)

while True:
    orden = input("Ingresa una orden (producto,cantidad / ver / checkout): ")

    if orden == "ver":
        mostrar_carrito()
    elif orden == "checkout":
        total = calcular_total()
        print(f"El total a pagar es: ${total}")
        break
    else:
        try:
            producto, cantidad = orden.split(",")
            agregar_al_carrito(int(producto), int(cantidad))
            print(f"Se agregaron {cantidad} unidades del producto {producto} al carrito.")
        except:
            print("Orden inválida. Por favor, intenta nuevamente.")