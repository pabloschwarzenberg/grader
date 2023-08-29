def agregar_producto(carro, producto, cantidad):
    if producto not in carro:
        carro[producto] = cantidad
    else:
        carro[producto] += cantidad

def imprimir_productos(carro):
    for producto, cantidad in carro.items():
        print(f"Producto {producto}: {cantidad} unidades")

def calcular_total(carro):
    total = 0

    if "1" in carro and "2" in carro and "3" in carro:
        total += (33.77 + 203 + 27.58) * 0.8 * carro.get("1", 0)
    if "4" in carro and "5" in carro:
        total += (348 + 51.19) * 0.85 * carro.get("4", 0)

    return round(total, 1)

if __name__ == "__main__":
    carro = {}

    while True:
        accion = input("¿Qué desea hacer? (agregar, ver, checkout): ")

        if accion == "agregar":
            datos = input("Ingrese el producto y la cantidad (producto,cantidad): ")
            producto, cantidad = datos.split(",")
            agregar_producto(carro, producto, int(cantidad))
            print("Producto agregado al carro.")

        elif accion == "ver":
            imprimir_productos(carro)

        elif accion == "checkout":
            total = calcular_total(carro)
            print(f"El total a pagar es: USD {total}")
            break

        else:
            print("Acción inválida. Por favor, intente nuevamente.")
