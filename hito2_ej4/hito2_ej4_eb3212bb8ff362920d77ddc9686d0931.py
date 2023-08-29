p1 = [1, "Pokemon X", 33.77]
p2 = [2, "Nintendo 3DS XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16, PlayStation 4", 51.19]

carrito = {}

def agregar_producto(producto, cantidad):
    if producto in carrito:
        carrito[producto] += cantidad
    else:
        carrito[producto] = cantidad

def ver_carrito():
    print("Productos en el carrito:")
    total = 0
    for producto, cantidad in carrito.items():
        nombre = eval("p" + str(producto))[1]
        precio = eval("p" + str(producto))[2]
        subtotal = precio * cantidad
        total += subtotal
        print("{nombre} x {cantidad}: ${subtotal:.2f}")
    print("Total: $" + str(total))

def aplicar_descuento():
    descuento = 0
    if all(producto in carrito for producto in [1, 2, 3]):
        descuento = 0.2
    elif all(producto in carrito for producto in [4, 5]):
        descuento = 0.15
    return descuento

def checkout():
    descuento = aplicar_descuento()
    total = 0
    for producto, cantidad in carrito.items():
        precio = eval("p" + str(producto))[2]
        subtotal = precio * cantidad
        total += subtotal
    total_descuento = total - (total * descuento)
    print("Total a pagar: $" + str(round(total_descuento, 2)))

while True:
    orden = input("Ingrese una orden (producto,cantidad / ver / checkout): ")
    if orden == "ver":
        ver_carrito()
    elif orden == "checkout":
        checkout()
        break
    else:
        producto, cantidad = orden.split(",")
        agregar_producto(int(producto), int(cantidad))