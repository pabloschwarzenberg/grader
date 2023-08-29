p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
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

    if "1" in carro and "2" in carro and "3" in carro:
        total += 33.77 * carro["1"]
        total += 203 * carro["2"]
        total += 27.58 * carro["3"]
        total *= 0.8

    if "4" in carro and "5" in carro:
        total += 348 * carro["4"]
        total += 51.19 * carro["5"]
        total *= 0.85

    return round(total, 1)


if __name__ == "__main__":
    carro = {}

    while True:
        orden = input("Ingrese la orden (producto,cantidad / ver / checkout): ")

        if orden == "ver":
            imprimir_carro(carro)
        elif orden == "checkout":
            total = calcular_descuento(carro)
            print(f"Total a pagar: USD {total}")
            break
        else:
            producto, cantidad = orden.split(",")
            agregar_producto(carro, producto, int(cantidad))      