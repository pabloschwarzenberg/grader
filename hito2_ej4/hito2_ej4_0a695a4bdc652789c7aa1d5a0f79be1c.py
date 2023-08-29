p1 = [1, "Pokemon X", 33.77]
p2 = [2, "Nintendo 3DS XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16, PlayStation 4", 51.19]

carro = []

def agregar_producto(producto, cantidad):
    producto_en_carro = next((p for p in carro if p[0] == producto), None)
    if producto_en_carro:
        producto_en_carro[1] += cantidad
    else:
        carro.append([producto, cantidad])

def ver_carro():
    for producto in carro:
        producto_id = producto[0]
        if producto_id == 1:
            print("Producto: Pokemon X para Nintendo 3DS")
            print("Cantidad:", producto[1])
            print("Precio unitario: USD 33.77")
            print("Precio total: USD", round(producto[1] * p1[2], 2))
        elif producto_id == 2:
            print("Producto: Nintendo 3DS XL")
            print("Cantidad:", producto[1])
            print("Precio unitario: USD 203")
            print("Precio total: USD", round(producto[1] * p2[2], 2))
        elif producto_id == 3:
            print("Producto: Mario Kart 7 para Nintendo 3DS")
            print("Cantidad:", producto[1])
            print("Precio unitario: USD 27.58")
            print("Precio total: USD", round(producto[1] * p3[2], 2))
        elif producto_id == 4:
            print("Producto: PlayStation 4")
            print("Cantidad:", producto[1])
            print("Precio unitario: USD 348.00")
            print("Precio total: USD", round(producto[1] * p4[2], 2))
        elif producto_id == 5:
            print("Producto: FIFA 16, PlayStation 4")
            print("Cantidad:", producto[1])
            print("Precio unitario: USD 51.19")
            print("Precio total: USD", round(producto[1] * p5[2], 2))
        print("--------------------")

def checkout():
    total = 0
    descuento = 0

    for producto in carro:
        producto_id = producto[0]
        cantidad = producto[1]
        if producto_id in [1, 2, 3]:
            descuento += cantidad * 0.2
        elif producto_id in [4, 5]:
            descuento += cantidad * 0.15

        if producto_id == 1:
            total += cantidad * p1[2]
        elif producto_id == 2:
            total += cantidad * p2[2]
        elif producto_id == 3:
            total += cantidad * p3[2]
        elif producto_id == 4:
            total += cantidad * p4[2]
        elif producto_id == 5:
            total += cantidad * p5[2]

    total -= descuento
    print("Total a pagar: USD", round(total, 2))

while True:
    orden = input("Ingrese su orden (producto,cantidad / ver / checkout): ")

    if orden == "ver":
        ver_carro()
    elif orden == "checkout":
        checkout()
        break
    else:
        try:
            producto, cantidad = orden.split(",")
            agregar_producto(int(producto), int(cantidad))
            print("Producto agregado al carro.")
        except ValueError:
            print("Orden inválida. Intente nuevamente.")

