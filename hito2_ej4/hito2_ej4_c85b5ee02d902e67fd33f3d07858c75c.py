p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
def agregar_producto(carro, producto, cantidad):
    producto = int(producto)
    cantidad = int(cantidad)

    if producto in carro:
        carro[producto] += cantidad
    else:
        carro[producto] = cantidad

    print(f"Se agregaron {cantidad} unidad(es) del producto {producto} al carro.")


def mostrar_productos(carro):
    if not carro:
        print("El carro de compras está vacío.")
    else:
        print("Productos en el carro:")
        for producto, cantidad in carro.items():
            print(f"Producto {producto}: {cantidad} unidad(es)")


def realizar_checkout(carro):
    total = 0.0

    for producto, cantidad in carro.items():
        if producto in [1, 2, 3]:
            total += cantidad * 0.8 * obtener_precio_producto(producto)
        elif producto in [4, 5]:
            total += cantidad * 0.85 * obtener_precio_producto(producto)

    print(f"Total a pagar: ${round(total, 1)}")


def obtener_precio_producto(producto):
    precios = {
        1: 33.77,
        2: 203,
        3: 27.58,
        4: 348.0,
        5: 51.19
    }

    return precios[producto]


if __name__ == "__main__":
    carro_de_compras = {}

    while True:
        orden = input("Ingrese una orden (agregar, ver, checkout): ")

        if orden == "agregar":
            producto, cantidad = input("Ingrese el producto y la cantidad (producto,cantidad): ").split(",")
            agregar_producto(carro_de_compras, producto, cantidad)
        elif orden == "ver":
            mostrar_productos(carro_de_compras)
        elif orden == "checkout":
            realizar_checkout(carro_de_compras)
            break
        else:
            print("Orden inválida. Intente nuevamente.")
      