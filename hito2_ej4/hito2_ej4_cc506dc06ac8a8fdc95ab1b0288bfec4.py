p1 = [1, "Juego Pokemon X para Nintendo 3DS", 33.77]
p2 = [2, "Nintendo 3DS XL", 203]
p3 = [3, "Juego Mario Kart 7 para Nintendo 3DS", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16, PlayStation 4", 51.19]

carro = {}

def agregar_producto(producto, cantidad):
    if producto not in carro:
        carro[producto] = cantidad
    else:
        carro[producto] += cantidad

def imprimir_carro():
    print("Productos en el carro:")
    for producto, cantidad in carro.items():
        print(f"Producto {producto}: {cantidad} unidades")

def calcular_total():
    total = 0
    descuento = 0

    if set([1, 2, 3]).issubset(carro.keys()):
        descuento = 0.2
    elif set([4, 5]).issubset(carro.keys()):
        descuento = 0.15

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

if __name__ == "__main__":
    while True:
        accion = input("¿Qué desea hacer? (agregar, ver, checkout, salir): ")
        
        if accion == "salir":
            break
        
        if accion == "agregar":
            entrada = input("Ingrese el producto y la cantidad (ejemplo: 1,2): ")
            producto, cantidad = map(int, entrada.split(","))
            agregar_producto(producto, cantidad)
            print("Producto agregado al carro.")
        
        elif accion == "ver":
            imprimir_carro()
        
        elif accion == "checkout":
            total = calcular_total()
            print(f"El total a pagar es: {total} USD")
            carro = {}  # Reiniciar el carro después de hacer el checkout
