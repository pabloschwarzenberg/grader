def agregar_producto(carro, producto, cantidad):
    carro[producto] = cantidad


def imprimir_carro(carro):
    for producto, cantidad in carro.items():
        print("Producto:", producto, "- Cantidad:", cantidad)


def calcular_descuento(carro):
    descuento = 0
    if carro.get("1", 0) > 0 and carro.get("2", 0) > 0 and carro.get("3", 0) > 0:
        descuento = 0.2
    elif carro.get("4", 0) > 0 and carro.get("5", 0) > 0:
        descuento = 0.15
    return descuento


def calcular_total(carro, descuento):
    precios = {
        "1": 33.77,
        "2": 203,
        "3": 27.58,
        "4": 348.00,
        "5": 51.19
    }
    total = 0
    for producto, cantidad in carro.items():
        total += precios[producto] * cantidad
    total -= total * descuento
    return round(total, 1)


carro = {}

while True:
    intento= 0

    while True:
        datos = input("Ingrese el producto y cantidad separados por coma (ejemplo: 5,2): ")
        producto, cantidad = datos.split(",")
        agregar_producto(carro, producto, int(cantidad))
        print("Producto agregado al carro.")
        intento = intento + 1
        if intento == 3:
            break

    descuento = calcular_descuento(carro)
    total = calcular_total(carro, descuento)
    print("Total a pagar (con descuento): USD", total)
    break