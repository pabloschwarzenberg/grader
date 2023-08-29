productos = {
    1: {'nombre': 'Juego Pokemon X para Nintendo 3DS', 'precio': 33.77},
    2: {'nombre': 'Nintendo 3DS XL', 'precio': 203.0},
    3: {'nombre': 'Juego Mario Kart 7 para Nintendo 3DS', 'precio': 27.58},
    4: {'nombre': 'PlayStation 4', 'precio': 348.0},
    5: {'nombre': 'FIFA 16, PlayStation 4', 'precio': 51.19}
}

carro = []

def agregar_al_carro(producto_id, cantidad):
    producto_id = int(producto_id)
    cantidad = int(cantidad)

    if producto_id in productos:
        carro.append((producto_id, cantidad))
        print(f"Se agregaron {cantidad} unidades del producto {producto_id} al carro.")
    else:
        print("El producto no existe.")

def mostrar_carro():
    if len(carro) == 0:
        print("El carro está vacío.")
    else:
        print("Productos en el carro:")
        for producto_id, cantidad in carro:
            producto = productos[producto_id]
            nombre = producto['nombre']
            precio = producto['precio']
            print(f"- {nombre}: {cantidad} unidades (USD {precio} c/u)")

def checkout():
    total = 0

    for producto_id, cantidad in carro:
        producto = productos[producto_id]
        precio = producto['precio']
        total += precio * cantidad

    if len(carro) >= 3 and set([1, 2, 3]).issubset(set([producto_id for producto_id, _ in carro])):
        descuento = total * 0.2
    elif len(carro) >= 2 and set([4, 5]).issubset(set([producto_id for producto_id, _ in carro])):
        descuento = total * 0.15
    else:
        descuento = 0

    total_con_descuento = total - descuento
    total_con_descuento = round(total_con_descuento, 1)

    print(f"Total a pagar: USD {total_con_descuento}")

if __name__ == "__main__":
    while True:
        orden = input("Ingrese una orden (agregar, ver, checkout): ")

        if orden == "agregar":
            producto_id, cantidad = input("Ingrese el producto y la cantidad: ").split(",")
            agregar_al_carro(producto_id, cantidad)
        elif orden == "ver":
            mostrar_carro()
        elif orden == "checkout":
            checkout()
            break
        else:
            print("Orden inválida.")


