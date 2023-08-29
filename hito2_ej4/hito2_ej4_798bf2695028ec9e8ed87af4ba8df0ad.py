def agregar_producto(carro, producto, cantidad):
    if producto in carro:
        carro[producto] += cantidad
    else:
        carro[producto] = cantidad

def mostrar_productos(carro):
    for producto, cantidad in carro.items():
        print("Producto {}: {} unidades".format(producto, cantidad))

def calcular_precio(carro):
    total = 0
    if "1" in carro and "2" in carro and "3" in carro:
        total += (33.77 + 203 + 27.58) * 0.8 * carro["1"]
    if "4" in carro and "5" in carro:
        total += (348 + 51.19) * 0.85 * carro["4"]
    return round(total, 1)

if __name__ == "__main__":
    carro = {}

    while True:
        orden = input("Ingresa una orden (agregar, ver, checkout): ")

        if orden == "agregar":
            producto, cantidad = input("Ingresa el producto y la cantidad: ").split(",")
            agregar_producto(carro, producto, int(cantidad))
        elif orden == "ver":
            mostrar_productos(carro)
        elif orden == "checkout":
            precio_total = calcular_precio(carro)
            print("El precio total es: USD {}".format(precio_total))
            break
