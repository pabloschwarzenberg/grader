p1 = [1, "Pokemon X", 33.77]
p2 = [2, "Nintendo 3DS XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16, PlayStation 4", 51.19]

carro = {}

def agregar_producto(producto, cantidad):
    if producto in carro:
        carro[producto] += cantidad
    else:
        carro[producto] = cantidad

def mostrar_productos():
    for producto, cantidad in carro.items():
        print(f"Producto {producto}: {cantidad} unidades")

def calcular_descuento():
    descuento = 0
    if 1 in carro and 2 in carro and 3 in carro:
        descuento = 0.2
    elif 4 in carro and 5 in carro:
        descuento = 0.15
    return descuento

def calcular_total():
    descuento = calcular_descuento()
    total = 0
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
    total -= total * descuento
    return round(total, 1)

while True:
    orden = input("Ingrese la orden (producto,cantidad / ver / checkout): ")
    if orden == "ver":
        mostrar_productos()
    elif orden == "checkout":
        total = calcular_total()
        print(f"El valor total de los productos en el carro es: USD {total}")
        break
    else:
        try:
            producto, cantidad = map(int, orden.split(","))
            if producto >= 1 and producto <= 5 and cantidad >= 1:
                agregar_producto(producto, cantidad)
            else:
                print("Orden inválida")
        except:
            print("Orden inválida")
