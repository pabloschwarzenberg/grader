def agregar_producto(carro, producto, cantidad):
    """
    Agrega un producto al carro de compras con la cantidad especificada.
    """
    if producto in carro:
        carro[producto] += cantidad
    else:
        carro[producto] = cantidad


def mostrar_carro(carro):
    """
    Muestra los productos en el carro de compras.
    """
    print("Productos en el carro:")
    for producto, cantidad in carro.items():
        print(f"Producto {producto}: {cantidad}")


def calcular_total(carro):
    """
    Calcula el total de los productos en el carro considerando los descuentos.
    """
    total = 0
    descuento_20 = {1, 2, 3}
    descuento_15 = {4, 5}

    for producto, cantidad in carro.items():
        if producto in descuento_20:
            total += calcular_precio_descuento(producto, cantidad, 0.2)
        elif producto in descuento_15:
            total += calcular_precio_descuento(producto, cantidad, 0.15)
        else:
            total += calcular_precio(producto, cantidad)

    return round(total, 1)


def calcular_precio(producto, cantidad):
    """
    Calcula el precio total de un producto sin descuento.
    """
    precios = {
        1: 33.77,
        2: 203,
        3: 27.58,
        4: 348,
        5: 51.19
    }
    return precios[producto] * cantidad


def calcular_precio_descuento(producto, cantidad, descuento):
    """
    Calcula el precio total de un producto con descuento.
    """
    precio_sin_descuento = calcular_precio(producto, cantidad)
    precio_con_descuento = precio_sin_descuento * (1 - descuento)
    return precio_con_descuento


if __name__ == "__main__":
    carro = {}

    while True:
        orden = input("Ingrese la orden (producto,cantidad / ver / checkout): ")

        if orden == "ver":
            mostrar_carro(carro)
        elif orden == "checkout":
            total = calcular_total(carro)
            print(f"Total a pagar: ${total}")
            break
        else:
            try:
                producto, cantidad = map(int, orden.split(","))
                agregar_producto(carro, producto, cantidad)
            except ValueError:
                print("Orden inválida. Intente nuevamente.")