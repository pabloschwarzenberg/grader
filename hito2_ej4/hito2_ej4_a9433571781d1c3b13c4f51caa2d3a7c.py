def agregar_producto(carro, producto, cantidad):
    if producto in carro:
        carro[producto] += cantidad
    else:
        carro[producto] = cantidad

def mostrar_productos(carro):
    print("Productos en el carrito:")
    for producto, cantidad in carro.items():
        print(f"Producto {producto}: Cantidad {cantidad}")

def calcular_precio(carro):
    descuento = 0
    precio_total = 0

    if "1" in carro and "2" in carro and "3" in carro:
        descuento = 0.2
    elif "4" in carro and "5" in carro:
        descuento = 0.15

    for producto, cantidad in carro.items():
        if producto == "1":
            precio_total += 33.77 * cantidad
        elif producto == "2":
            precio_total += 203 * cantidad
        elif producto == "3":
            precio_total += 27.58 * cantidad
        elif producto == "4":
            precio_total += 348 * cantidad
        elif producto == "5":
            precio_total += 51.19 * cantidad

    precio_total -= precio_total * descuento

    return round(precio_total, 1)

# Diccionario para almacenar los productos en el carrito
carro = {}

while True:
    orden = input("Ingrese su orden (agregar, ver, checkout): ")

    if orden == "agregar":
        entrada = input("Ingrese el producto y la cantidad (producto,cantidad): ")
        producto, cantidad = entrada.split(",")
        agregar_producto(carro, producto, int(cantidad))
        print("Producto agregado al carrito.")
    elif orden == "ver":
        mostrar_productos(carro)
    elif orden == "checkout":
        precio_total = calcular_precio(carro)
        print(f"Total a pagar: USD {precio_total}")
        break
    else:
        print("Orden inválida. Intente nuevamente.")