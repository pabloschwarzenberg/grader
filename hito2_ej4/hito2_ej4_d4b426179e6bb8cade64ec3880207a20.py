def agregar_producto(carrito, producto, cantidad):
    if producto == "1":
        carrito["Juego Pokemon X para Nintendo 3DS"] = cantidad
    elif producto == "2":
        carrito["Nintendo 3DS XL"] = cantidad
    elif producto == "3":
        carrito["Juego Mario Kart 7 para Nintendo 3DS"] = cantidad
    elif producto == "4":
        carrito["PlayStation 4"] = cantidad
    elif producto == "5":
        carrito["FIFA 16, PlayStation 4"] = cantidad


def mostrar_productos(carrito):
    if len(carrito) == 0:
        print("El carrito está vacío.")
    else:
        for producto, cantidad in carrito.items():
            print(f"{producto}: {cantidad} unidades")


def calcular_total(carrito):
    precios = {
        "Juego Pokemon X para Nintendo 3DS": 33.77,
        "Nintendo 3DS XL": 203,
        "Juego Mario Kart 7 para Nintendo 3DS": 27.58,
        "PlayStation 4": 348.00,
        "FIFA 16, PlayStation 4": 51.19
    }

    total = 0

    if "1" in carrito and "2" in carrito and "3" in carrito:
        total += (precios["Juego Pokemon X para Nintendo 3DS"] + precios["Nintendo 3DS XL"]
                  + precios["Juego Mario Kart 7 para Nintendo 3DS"]) * 0.8
    elif "4" in carrito and "5" in carrito:
        total += (precios["PlayStation 4"] + precios["FIFA 16, PlayStation 4"]) * 0.85
    else:
        for producto, cantidad in carrito.items():
            total += precios[producto] * cantidad

    total = round(total, 1)
    return total


if __name__ == "__main__":
    carrito = {}

    while True:
        orden = input("Ingrese su orden (agregar, ver, checkout): ")

        if orden == "agregar":
            producto, cantidad = input("Ingrese el producto y cantidad (ejemplo: 1,2): ").split(",")
            agregar_producto(carrito, producto, int(cantidad))
        elif orden == "ver":
            mostrar_productos(carrito)
        elif orden == "checkout":
            total = calcular_total(carrito)
            print(f"Total a pagar: USD {total}")
            break