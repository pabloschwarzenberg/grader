def agregar_producto(carro, producto, cantidad):
    if producto in carro:
        carro[producto] += cantidad
    else:
        carro[producto] = cantidad


def mostrar_productos(carro, productos):
    for producto, cantidad in carro.items():
        p = productos[int(producto) - 1]
        print(f"Producto {producto}: {p[1]} - {cantidad} unidad(es)")


def calcular_total(carro, productos):
    total = 0
    
    for producto, cantidad in carro.items():
        p = productos[int(producto) - 1]
        precio = p[2]
        
        if producto in ["1", "2", "3"]:
            total += cantidad * 0.8 * precio
        elif producto in ["4", "5"]:
            total += cantidad * 0.85 * precio
        else:
            print(f"Producto inválido: {producto}")
    
    return round(total, 1)


if __name__ == "__main__":
    productos = [
        [1, "Juego Pokemon X para Nintendo 3DS", 33.77],
        [2, "Nintendo 3DS XL", 203],
        [3, "Juego Mario Kart 7 para Nintendo 3DS", 27.58],
        [4, "PlayStation 4", 348.00],
        [5, "FIFA 16, PlayStation 4", 51.19]
    ]
    
    carro = {}
    
    while True:
        orden = input("Ingrese la orden (agregar, ver, checkout): ")
        
        if orden == "agregar":
            producto, cantidad = input("Ingrese el producto y la cantidad (producto,cantidad): ").split(",")
            agregar_producto(carro, producto, int(cantidad))
        elif orden == "ver":
            mostrar_productos(carro, productos)
        elif orden == "checkout":
            total = calcular_total(carro, productos)
            print(f"El total a pagar es: USD {total}")
            break
        else:
            print("Orden inválida. Intente nuevamente.")
