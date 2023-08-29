p1 = [1, "Pokemon X", 33.77]
p2 = [2, "Nintendo XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16", 51.19]

carro = {}

def agregar_producto(carro, producto, cantidad):
    if producto in carro:
        carro[producto] += cantidad
    else:
        carro[producto] = cantidad

def mostrar_productos(carro):
    for producto, cantidad in carro.items():
        print(f"Producto {producto}: {cantidad} unidades")

def calcular_total(carro, productos):
    descuento_20 = {1, 2, 3}
    descuento_15 = {4, 5}

    total = 0

    for producto, cantidad in carro.items():
        for p in productos:
            if producto == p[0]:
                precio = p[2]
                if producto in descuento_20:
                    precio *= 0.8
                elif producto in descuento_15:
                    precio *= 0.85
                total += precio * cantidad

    return round(total, 1)

while True:
    accion = input("Ingrese una acción (agregar, ver, checkout): ")

    if accion == "agregar":
        datos_producto = input("Ingrese el producto y cantidad (producto,cantidad): ")
        producto, cantidad = datos_producto.split(",")
        agregar_producto(carro, int(producto), int(cantidad))
    elif accion == "ver":
        mostrar_productos(carro)
    elif accion == "checkout":
        total = calcular_total(carro, [p1, p2, p3, p4, p5])
        print(f"Total a pagar: {total}")
        break