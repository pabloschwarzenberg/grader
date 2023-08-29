def agregar_producto(carro, producto, cantidad):
    if producto in carro:
        carro[producto] += cantidad
    else:
        carro[producto] = cantidad

def mostrar_productos(carro):
    for producto, cantidad in carro.items():
        print(f"Producto {producto}: {cantidad} unidades")

def calcular_descuento(carro):
    productos = carro.keys()
    if {"1", "2", "3"}.issubset(productos):
        return 0.8  # 20% de descuento
    elif {"4", "5"}.issubset(productos):
        return 0.85  # 15% de descuento
    else:
        return 1.0  # Sin descuento

def calcular_total(carro):
    descuento = calcular_descuento(carro)
    total = 0.0
    precios = {
        "1": 33.77,
        "2": 203.0,
        "3": 27.58,
        "4": 348.0,
        "5": 51.19
    }
    for producto, cantidad in carro.items():
        total += precios[producto] * cantidad
    return round(total * descuento, 1)

if __name__ == "__main__":
    carro = {}
    
    while True:
        orden = input("Ingrese una orden (agregar, ver, checkout): ")
        
        if orden == "agregar":
            producto, cantidad = input("Ingrese el producto y la cantidad: ").split(",")
            agregar_producto(carro, producto, int(cantidad))
        elif orden == "ver":
            mostrar_productos(carro)
        elif orden == "checkout":
            total = calcular_total(carro)
            print(f"El total a pagar es: USD {total}")
            break
        else:
            print("Orden inválida. Intente nuevamente.")
