PRODUCTOS = {
    1: ("Juego Pokemon X para Nintendo 3DS", 33.77),
    2: ("Nintendo 3DS XL", 203),
    3: ("Juego Mario Kart 7 para Nintendo 3DS", 27.58),
    4: ("PlayStation 4", 348.00),
    5: ("FIFA 16, PlayStation 4", 51.19)
}

carro = {}

def agregar_producto(producto, cantidad):
    if producto in carro:
        carro[producto] += cantidad
    else:
        carro[producto] = cantidad

def mostrar_carro():
    for producto, cantidad in carro.items():
        nombre, precio = PRODUCTOS[producto]
        print(f"Producto: {nombre}, Cantidad: {cantidad}, Precio unitario: ${precio}")

def calcular_total():
    total = 0

    if set([1, 2, 3]).issubset(carro.keys()):
        total += (PRODUCTOS[1][1] + PRODUCTOS[2][1] + PRODUCTOS[3][1]) * 0.8
    if set([4, 5]).issubset(carro.keys()):
        total += (PRODUCTOS[4][1] + PRODUCTOS[5][1]) * 0.85
    for producto, cantidad in carro.items():
        if producto not in [1, 2, 3, 4, 5]:
            total += PRODUCTOS[producto][1] * cantidad

    return round(total, 1)

if __name__ == "__main__":
    while True:
        orden = input("Ingrese una orden (producto,cantidad / ver / checkout): ")

        if orden == "ver":
            mostrar_carro()
        elif orden == "checkout":
            total = calcular_total()
            print(f"Total a pagar: ${total}")
            break
        else:
            producto, cantidad = orden.split(",")
            agregar_producto(int(producto), int(cantidad))

      