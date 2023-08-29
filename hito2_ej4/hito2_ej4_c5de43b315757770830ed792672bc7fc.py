p1 = [1, "Juego Pokemon X para Nintendo 3DS", 33.77]
p2 = [2, "Nintendo 3DS XL", 203]
p3 = [3, "Juego Mario Kart 7 para Nintendo 3DS", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16, PlayStation 4", 51.19]

carro = {}  # Diccionario para almacenar los productos en el carro

def agregar_producto(producto, cantidad):
    if producto not in carro:
        carro[producto] = 0
    carro[producto] += cantidad

def ver_productos():
    for producto, cantidad in carro.items():
        if producto == 1:
            print(f"{p1[1]} - Cantidad: {cantidad}")
        elif producto == 2:
            print(f"{p2[1]} - Cantidad: {cantidad}")
        elif producto == 3:
            print(f"{p3[1]} - Cantidad: {cantidad}")
        elif producto == 4:
            print(f"{p4[1]} - Cantidad: {cantidad}")
        elif producto == 5:
            print(f"{p5[1]} - Cantidad: {cantidad}")

def checkout():
    total = 0
    descuento = 0

    # Calcular el total sin descuento
    for producto, cantidad in carro.items():
        if producto == 1:
            total += p1[2] * cantidad
        elif producto == 2:
            total += p2[2] * cantidad
        elif producto == 3:
            total += p3[2] * cantidad
        elif producto == 4:
            total += p4[2] * cantidad
        elif producto == 5:
            total += p5[2] * cantidad

    # Aplicar descuento según los productos en el carro
    if set(carro.keys()) == {1, 2, 3}:
        descuento = total * 0.2
    elif set(carro.keys()) == {4, 5}:
        descuento = total * 0.15

    total -= descuento
    total = round(total, 1)

    print(f"Total a pagar: USD {total}")

# Obtener las órdenes del usuario
while True:
    orden = input("Ingrese una orden (producto,cantidad / ver / checkout): ")

    if orden == "ver":
        ver_productos()
    elif orden == "checkout":
        checkout()
        break
    else:
        try:
            producto, cantidad = map(int, orden.split(","))
            agregar_producto(producto, cantidad)
        except ValueError:
            print("Orden inválida. Intente nuevamente.")
