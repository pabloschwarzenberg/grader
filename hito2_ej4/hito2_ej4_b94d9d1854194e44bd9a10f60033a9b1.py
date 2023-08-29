def agregar_producto(carro, producto, cantidad):
    if producto in carro:
        carro[producto] += cantidad
    else:
        carro[producto] = cantidad

def mostrar_productos(carro):
    for producto, cantidad in carro.items():
        print(f"Producto {producto}: {cantidad} unidades")

def calcular_total(carro):
    descuento = 0
    total = 0
    if "1" in carro and "2" in carro and "3" in carro:
        descuento = 0.2
    elif "4" in carro and "5" in carro:
        descuento = 0.15

    for producto, cantidad in carro.items():
        if producto == "1":
            total += cantidad * 33.77
        elif producto == "2":
            total += cantidad * 203
        elif producto == "3":
            total += cantidad * 27.58
        elif producto == "4":
            total += cantidad * 348
        elif producto == "5":
            total += cantidad * 51.19

    total -= total * descuento
    return round(total, 1)

carro = {}

while True:
    orden = input("Ingrese una orden (agregar, ver, checkout): ")

    if orden == "agregar":
        datos = input("Ingrese el producto y la cantidad (producto,cantidad): ")
        producto, cantidad = datos.split(",")
        agregar_producto(carro, producto, int(cantidad))
        print("Producto agregado al carro.")

    elif orden == "ver":
        mostrar_productos(carro)

    elif orden == "checkout":
        total = calcular_total(carro)
        print(f"El total a pagar es: USD {total}")
        break

    else:
        print("Orden inválida. Intente nuevamente.")
