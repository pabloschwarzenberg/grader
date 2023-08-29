def agregar_al_carro(carro, producto, cantidad):
    if producto in carro:
        carro[producto] += cantidad
    else:
        carro[producto] = cantidad

def mostrar_carro(carro):
    print("Productos en el carro:")
    for producto, cantidad in carro.items():
        print(f"Producto {producto}: {cantidad}")

def calcular_precio(producto, cantidad):
    precios = {
        1: 33.77,
        2: 203.00,
        3: 27.58,
        4: 348.00,
        5: 51.19
    }
    return precios[producto] * cantidad

def aplicar_descuento(carro):
    productos_descuento_1 = {1, 2, 3}
    productos_descuento_2 = {4, 5}

    total_descuento_1 = 0
    total_descuento_2 = 0

    for producto, cantidad in carro.items():
        if producto in productos_descuento_1:
            total_descuento_1 += calcular_precio(producto, cantidad)
        elif producto in productos_descuento_2:
            total_descuento_2 += calcular_precio(producto, cantidad)

    descuento_1 = total_descuento_1 * 0.2
    descuento_2 = total_descuento_2 * 0.15

    return descuento_1 + descuento_2

def checkout(carro):
    subtotal = 0
    for producto, cantidad in carro.items():
        subtotal += calcular_precio(producto, cantidad)

    descuento = aplicar_descuento(carro)
    total = subtotal - descuento

    print("Carro de compras:")
    mostrar_carro(carro)
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Descuento: {descuento:.2f}")
    print(f"Total a pagar: {total:.2f}")

carro = {}

while True:
    orden = input("Ingresa la orden (producto,cantidad / ver / checkout): ")
    if orden == "ver":
        mostrar_carro(carro)
    elif orden == "checkout":
        checkout(carro)
        break
    else:
        producto, cantidad = orden.split(",")
        agregar_al_carro(carro, int(producto), int(cantidad))
