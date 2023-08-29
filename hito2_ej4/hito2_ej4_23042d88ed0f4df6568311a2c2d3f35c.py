def agregar_producto(carro, producto, cantidad):
    if producto in carro:
        carro[producto] += cantidad
    else:
        carro[producto] = cantidad

def mostrar_productos(carro):
    for producto, cantidad in carro.items():
        print(f"Producto {producto}: {cantidad} unidades")

def checkout(carro):
    total = 0
    descuento = 0

    # Verificar descuentos
    if "1" in carro and "2" in carro and "3" in carro:
        descuento = 0.2
    elif "4" in carro and "5" in carro:
        descuento = 0.15

    # Calcular total
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

    # Aplicar descuento
    total -= total * descuento

    # Imprimir total redondeado a un decimal
    print(f"Total: {round(total, 1)}")

if __name__ == "__main__":
    carro = {}

    while True:
        orden = input("Ingrese una orden (agregar, ver, checkout): ")

        if orden == "agregar":
            producto, cantidad = input("Ingrese el producto y la cantidad: ").split(",")
            agregar_producto(carro, producto, int(cantidad))
        elif orden == "ver":
            mostrar_productos(carro)
        elif orden == "checkout":
            checkout(carro)
            break
        else:
            print("Orden inválida. Intente nuevamente.")
