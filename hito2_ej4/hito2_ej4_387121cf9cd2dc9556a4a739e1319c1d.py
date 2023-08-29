def agregar_al_carro(carro, producto, cantidad):
    for item in carro:
        if item[0] == producto:
            item[1] += cantidad
            return
    carro.append([producto, cantidad])

def mostrar_carro(carro):
    print("Productos en el carro:")
    for item in carro:
        producto = obtener_producto_por_codigo(item[0])
        print("Código: {}, Nombre: {}, Cantidad: {}".format(item[0], producto[1], item[1]))

def obtener_producto_por_codigo(codigo):
    productos = {
        1: p1,
        2: p2,
        3: p3,
        4: p4,
        5: p5
    }
    return productos[codigo]

def calcular_precio_total(carro):
    subtotal = 0
    for item in carro:
        producto = obtener_producto_por_codigo(item[0])
        subtotal += producto[2] * item[1]

    descuento = 0
    if len(carro) >= 3 and all(item[0] in [1, 2, 3] for item in carro):
        descuento = 0.2
    elif len(carro) >= 2 and all(item[0] in [4, 5] for item in carro):
        descuento = 0.15

    precio_total = subtotal - (subtotal * descuento)
    return round(precio_total, 1)

p1 = [1, "Pokemon X", 33.77]
p2 = [2, "Nintendo XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16", 51.19]

carro = []

while True:
    accion = input("¿Qué acción desea realizar? (agregar, ver, checkout): ")

    if accion == "agregar":
        entrada = input("Ingrese el código del producto y la cantidad (Ejemplo: 5,2): ")
        codigo, cantidad = map(int, entrada.split(","))
        agregar_al_carro(carro, codigo, cantidad)
        print("Producto agregado al carro.")

    elif accion == "ver":
        mostrar_carro(carro)

    elif accion == "checkout":
        precio_total = calcular_precio_total(carro)
        print("Precio total a pagar: ${}".format(precio_total))
        break

    else:
        print("Acción inválida. Intente nuevamente.")

