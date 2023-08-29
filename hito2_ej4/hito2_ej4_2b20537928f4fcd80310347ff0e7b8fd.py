def agregar_producto(carro, producto, cantidad):
    if producto[0] in carro:
        carro[producto[0]] += cantidad
    else:
        carro[producto[0]] = cantidad

def mostrar_productos(carro, productos):
    for producto, cantidad in carro.items():
        p = next(item for item in productos if item[0] == producto)
        print(f"Producto {producto}: {cantidad} unidades - {p[1]} (${p[2]})")

def calcular_total(carro, productos):
    total = 0
    
    if 1 in carro and 2 in carro and 3 in carro:
        descuento = sum(producto[2] for producto in productos if producto[0] in [1, 2, 3]) * 0.2
        total += descuento * carro[1]
        del carro[1]
        del carro[2]
        del carro[3]
    
    if 4 in carro and 5 in carro:
        descuento = sum(producto[2] for producto in productos if producto[0] in [4, 5]) * 0.15
        total += descuento * carro[4]
        del carro[4]
        del carro[5]
    
    for producto, cantidad in carro.items():
        p = next(item for item in productos if item[0] == producto)
        total += p[2] * cantidad
    
    return round(total, 1)

if __name__ == "__main__":
    productos = [
        [1, "Pokemon X", 33.77],
        [2, "Nintendo 3DS XL", 203],
        [3, "Mario Kart 7", 27.58],
        [4, "PlayStation 4", 348.00],
        [5, "FIFA 16, PlayStation 4", 51.19]
    ]
    
    carro = {}
    
    while True:
        accion = input("Ingrese una acción (agregar, ver, checkout): ")
        
        if accion == "agregar":
            datos = input("Ingrese el producto y la cantidad (ejemplo: 5,2): ")
            producto, cantidad = datos.split(",")
            agregar_producto(carro, int(producto), int(cantidad))
        elif accion == "ver":
            mostrar_productos(carro, productos)
        elif accion == "checkout":
            total = calcular_total(carro, productos)
            print(f"Total a pagar: ${total}")
            break
