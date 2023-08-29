def agregar_producto(carro, producto, cantidad):
    carro[producto] = carro.get(producto, 0) + cantidad

def calcular_descuento(carro):
    productos = set(carro.keys())
    if productos == {1, 2, 3}:
        descuento = 0.2
    elif productos == {4, 5}:
        descuento = 0.15
    else:
        descuento = 0.0
    return descuento

def imprimir_carro(carro):
    for producto, cantidad in carro.items():
        print("Producto ", producto, ": ", cantidad, "unidades")

def calcular_total(carro, descuento):
    precios = {
        1: 33.77,
        2: 203,
        3: 27.58,
        4: 348.00,
        5: 51.19
    }
    total = sum(cantidad * precios[producto] for producto, cantidad in carro.items())
    total_descuento = total - (total * descuento)
    return round(total_descuento, 1)

if __name__ == "__main__":
    carro = {}

    while True:
        orden = input("Ingrese una orden (agregar, ver, checkout): ")

        if orden == "agregar":
            entrada = input("Ingrese el producto y cantidad: ")
            producto, cantidad = map(int, entrada.split(","))
            agregar_producto(carro, producto, cantidad)
            print("Producto agregado al carro.")

        elif orden == "ver":
            imprimir_carro(carro)

        elif orden == "checkout":
            descuento = calcular_descuento(carro)
            total = calcular_total(carro, descuento)
            print("Total a pagar:", total)
            break

        else:
            print("Orden inválida. Intente nuevamente.")
