def agregar_producto(carrito, producto, cantidad):
    if producto[0] in carrito:
        carrito[producto[0]] += cantidad
    else:
        carrito[producto[0]] = cantidad

def mostrar_carrito(carrito, productos):
    for producto, cantidad in carrito.items():
        info_producto = next((p for p in productos if p[0] == producto), None)
        if info_producto:
            print("Producto {}: {} unidades (}, USD {})".format(producto, cantidad, info_producto[1], info_producto[2]))

def hacer_checkout(carrito, productos):
    descuento = 0
    total = 0

    if "1" in carrito and "2" in carrito and "3" in carrito:
        descuento = 0.2
    elif "4" in carrito and "5" in carrito:
        descuento = 0.15

    for producto, cantidad in carrito.items():
        info_producto = next((p for p in productos if p[0] == producto), None)
        if info_producto:
            total += info_producto[2] * cantidad

    total -= total * descuento
    total = round(total, 1)
    print("Total a pagar: USD {}".format(total))

if __name__ == "__main__":
    p1 = [1, "Pokemon X", 33.77]
    p2 = [2, "Nintendo XL", 203]
    p3 = [3, "Mario Kart 7", 27.58]
    p4 = [4, "PlayStation 4", 348.00]
    p5 = [5, "FIFA 16", 51.19]

    productos = [p1, p2, p3, p4, p5]
    carrito = {}

    while True:
        orden = input("Ingrese una orden (agregar, ver, checkout): ")

        if orden == "agregar":
            producto, cantidad = input("Ingrese el producto y cantidad (producto,cantidad): ").split(",")
            producto = int(producto)
            cantidad = int(cantidad)
            agregar_producto(carrito, productos[producto-1], cantidad)
        elif orden == "ver":
            mostrar_carrito(carrito, productos)
        elif orden == "checkout":
            hacer_checkout(carrito, productos)
            break
        else:
            print("Orden inválida. Intente nuevamente.")

      