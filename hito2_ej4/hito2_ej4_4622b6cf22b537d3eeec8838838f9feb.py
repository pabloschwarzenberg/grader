p1 = [1, "Juego Pokemon X para Nintendo 3DS", 33.77]
p2 = [2, "Nintendo 3DS XL", 203]
p3 = [3, "Juego Mario Kart 7 para Nintendo 3DS", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16, PlayStation 4", 51.19]

carro = []

def agregar_producto(producto, cantidad):
    global carro
    for i in range(cantidad):
        carro.append(producto)
    print("Se agregaron", cantidad, "unidades del producto", producto[0], "al carro.")

def ver_carro():
    global carro
    if len(carro) == 0:
        print("El carro está vacío.")
    else:
        print("Productos en el carro:")
        for producto in carro:
            print(producto[0], "-", producto[1])

def checkout():
    global carro
    total = 0.0
    descuento = 0.0

    for producto in carro:
        total += producto[2]

    productos_en_carro = set([producto[0] for producto in carro])

    if productos_en_carro.issuperset([1, 2, 3]):
        descuento = total * 0.2
    elif productos_en_carro.issuperset([4, 5]):
        descuento = total * 0.15

    total -= descuento

    print("Checkout:")
    print("Total: $", round(total, 1))
    carro = []

while True:
    orden = input("Ingrese una orden (producto,cantidad / ver / checkout): ")

    if orden == "ver":
        ver_carro()
    elif orden == "checkout":
        checkout()
        break
    else:
        try:
            producto, cantidad = orden.split(",")
            producto = int(producto)
            cantidad = int(cantidad)

            if producto == 1:
                agregar_producto(p1, cantidad)
            elif producto == 2:
                agregar_producto(p2, cantidad)
            elif producto == 3:
                agregar_producto(p3, cantidad)
            elif producto == 4:
                agregar_producto(p4, cantidad)
            elif producto == 5:
                agregar_producto(p5, cantidad)
            else:
                print("Producto inválido.")
        except ValueError:
            print("Orden inválida. Asegúrese de ingresarla en el formato correcto.")
