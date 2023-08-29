# Precios de los productos
precios = {
    1: 33.77,
    2: 203.00,
    3: 27.58,
    4: 348.00,
    5: 51.19
}

# Carro de compras
carro = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0
}

# Función para agregar productos al carro
def agregar_producto(producto, cantidad):
    producto = int(producto)
    cantidad = int(cantidad)
    carro[producto] += cantidad

# Función para mostrar los productos en el carro
def ver_productos():
    for producto, cantidad in carro.items():
        if cantidad > 0:
            print(f"Producto {producto}: Cantidad {cantidad}")

# Función para calcular el total con descuentos
def calcular_total():
    total = 0.0

    # Descuento del 20% para los productos 1, 2 y 3
    if carro[1] > 0 and carro[2] > 0 and carro[3] > 0:
        total += (precios[1] + precios[2] + precios[3]) * 0.8 * carro[1]
        carro[1] = 0
        carro[2] = 0
        carro[3] = 0

    # Descuento del 15% para los productos 4 y 5
    if carro[4] > 0 and carro[5] > 0:
        total += (precios[4] + precios[5]) * 0.85 * carro[4]
        carro[4] = 0
        carro[5] = 0

    # Calcular el total sin descuento para los productos restantes
    for producto, cantidad in carro.items():
        total += precios[producto] * cantidad

    return round(total, 1)

# Programa principal
while True:
    orden = input("Ingrese una orden (producto,cantidad / ver / checkout): ")

    if orden == "ver":
        ver_productos()
    elif orden == "checkout":
        total = calcular_total()
        print(f"Total a pagar: USD {total}")
        break
    else:
        try:
            producto, cantidad = orden.split(",")
            agregar_producto(producto, cantidad)
        except ValueError:
            print("Orden inválida. Por favor, ingrese una orden válida.")
