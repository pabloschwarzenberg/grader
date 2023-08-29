precios = {
    1: 33.77,
    2: 203.00,
    3: 27.58,
    4: 348.00,
    5: 51.19
}

carro = {}

def agregar_producto(producto, cantidad):
    if producto in carro:
        carro[producto] += cantidad
    else:
        carro[producto] = cantidad

def ver_productos():
    for producto, cantidad in carro.items():
        print(f"Producto {producto}: {cantidad} unidades")

def calcular_total():
    total = 0
    for producto, cantidad in carro.items():
        total += precios[producto] * cantidad

    descuento = 0
    if set([1, 2, 3]).issubset(carro.keys()):
        descuento = total * 0.2
    elif set([4, 5]).issubset(carro.keys()):
        descuento = total * 0.15

    total -= descuento
    return round(total, 1)

if __name__ == "__main__":
    while True:
        orden = input("Ingrese una orden (producto,cantidad / ver / checkout): ")
        
        if orden == "ver":
            ver_productos()
        elif orden == "checkout":
            total = calcular_total()
            print(f"Total a pagar: USD {total}")
            break
        else:
            try:
                producto, cantidad = map(int, orden.split(","))
                agregar_producto(producto, cantidad)
                print("Producto agregado al carro")
            except:
                print("Orden inválida")