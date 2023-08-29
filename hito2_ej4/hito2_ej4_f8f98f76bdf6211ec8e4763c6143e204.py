p1 = [1, "Pokemon X", 33.77]
p2 = [2, "Nintendo XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16", 51.19]

carro = []

def agregar_producto(producto, cantidad):
    carro.append((producto, cantidad))

def ver_carro():
    if len(carro) == 0:
        print("Carro vacío")
    else:
        for producto, cantidad in carro:
            nombre = ""
            precio = 0.0
            if producto == 1:
                nombre = p1[1]
                precio = p1[2]
            elif producto == 2:
                nombre = p2[1]
                precio = p2[2]
            elif producto == 3:
                nombre = p3[1]
                precio = p3[2]
            elif producto == 4:
                nombre = p4[1]
                precio = p4[2]
            elif producto == 5:
                nombre = p5[1]
                precio = p5[2]
            print("Producto {}: {} - {} unidades".format(producto, nombre, cantidad))

def calcular_total():
    total = 0.0
    for producto, cantidad in carro:
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
    return total

def aplicar_descuento(total):
    descuento = 0.0
    if (1 in [producto for producto, _ in carro]) and (2 in [producto for producto, _ in carro]) and (3 in [producto for producto, _ in carro]):
        descuento = total * 0.2
    elif (4 in [producto for producto, _ in carro]) and (5 in [producto for producto, _ in carro]):
        descuento = total * 0.15
    return total - descuento

def checkout():
    total = calcular_total()
    if total > 0:
        total_descuento = aplicar_descuento(total)
        print("{:.1f}".format(total_descuento))
    else:
        print("Carro vacío")

def carro_de_compras():
    while True:
        orden = input("Ingrese el producto y cantidad (producto,cantidad) o escriba 'checkout' para finalizar: ")
        if orden.lower() == "checkout":
            checkout()
            break
        else:
            try:
                producto, cantidad = map(int, orden.split(","))
                agregar_producto(producto, cantidad)
            except ValueError:
                print("Entrada inválida. Intente nuevamente.")

carro_de_compras()