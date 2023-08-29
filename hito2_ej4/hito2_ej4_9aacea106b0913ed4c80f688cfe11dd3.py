def agregar_producto(carro, producto, cantidad):
    if producto in carro:
        carro[producto] += cantidad
    else:
        carro[producto] = cantidad

def imprimir_carro(carro):
    print("Productos en el carro:")
    for producto, cantidad in carro.items():
        print(f"Producto {producto}: {cantidad} unidades")

def calcular_descuento(carro):
    total = 0
    descuento = 0

    if "1" in carro and "2" in carro and "3" in carro:
        descuento = 0.2
    elif "4" in carro and "5" in carro:
        descuento = 0.15

    for producto, cantidad in carro.items():
        if producto == "1":
            total += 33.77 * cantidad
        elif producto == "2":
            total += 203 * cantidad
        elif producto == "3":
            total += 27.58 * cantidad
        elif producto == "4":
            total += 348 * cantidad
        elif producto == "5":
            total += 51.19 * cantidad

    total -= total * descuento
    return round(total, 2)

carro = {}

while True:
    orden = input("Ingrese una orden (agregar, ver, checkout): ")

    if orden == "agregar":
        producto, cantidad = input("Ingrese el producto y la cantidad separados por coma: ").split(",")
        agregar_producto(carro, producto.strip(), int(cantidad))
    elif orden == "ver":
        imprimir_carro(carro)
    elif orden == "checkout":
        total = calcular_descuento(carro)
        print(f"Total a pagar: ${total}")
        break
    else:
        print("Orden inválida. Intente nuevamente.")
