def agregar_producto(carro, producto, cantidad):
    if producto in carro:
        carro[producto] += cantidad
    else:
        carro[producto] = cantidad

def ver_productos(carro):
    print("Productos en el carro:")
    for producto, cantidad in carro.items():
        print(f"Producto {producto}: {cantidad}")

def checkout(carro):
    total = 0
    for producto, cantidad in carro.items():
        if producto == "1" or producto == "2" or producto == "3":
            total += cantidad * 0.8 * precios[producto]
        elif producto == "4" or producto == "5":
            total += cantidad * 0.85 * precios[producto]
        else:
            print("Producto inválido")

    print(f"Total a pagar: ${round(total, 1)}")

if __name__ == "__main__":
    carro = {}
    precios = {
        "1": 33.77,
        "2": 203,
        "3": 27.58,
        "4": 348.00,
        "5": 51.19
    }