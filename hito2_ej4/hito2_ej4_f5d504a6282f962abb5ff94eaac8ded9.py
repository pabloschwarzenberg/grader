# Precios de los productos
precios = {
    1: 33.77,
    2: 203.00,
    3: 27.58,
    4: 348.00,
    5: 51.19
}

# Descuentos por combinaciones de productos
descuentos = {
    (1, 2, 3): 0.20,
    (4, 5): 0.15
}

carro = {}  # Diccionario para almacenar los productos agregados al carro

def agregar_producto(producto, cantidad):
    producto = int(producto)
    cantidad = int(cantidad)
    if producto in carro:
        carro[producto] += cantidad
    else:
        carro[producto] = cantidad

def mostrar_productos():
    for producto, cantidad in carro.items():
        print(f"Producto {producto}: {cantidad} unidad(es)")

def calcular_total():
    total = 0.0
    for producto, cantidad in carro.items():
        total += precios[producto] * cantidad

    for combinacion, descuento in descuentos.items():
        if set(combinacion).issubset(carro.keys()):
            total *= (1 - descuento)

    return round(total, 1)

if __name__ == "__main__":
    while True:
        orden = input("Ingrese una orden (producto,cantidad / ver / checkout): ")

        if orden == "ver":
            mostrar_productos()
        elif orden == "checkout":
            total = calcular_total()
            print(f"Total a pagar: USD {total}")
            break
        else:
            producto, cantidad = orden.split(",")
            agregar_producto(producto, cantidad)
