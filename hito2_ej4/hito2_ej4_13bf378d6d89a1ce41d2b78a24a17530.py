productos = {
    1:{"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2:{"nombre": "Nintendo 3DS XL", "precio": 203},
    3:{"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4:{"nombre": "PlayStation 4", "precio": 348.00},
    5:{"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}

carro = {}

def agregar_producto(producto, cantidad):
    if producto in productos:
        if producto in carro:
            carro[producto] += cantidad
        else:
            carro[producto] = cantidad
        print(f"Se agregaron {cantidad} unidad(es) del producto {producto} al carro.")
    else:
        print("El producto ingresado no es válido.")

def mostrar_carro():
    if len(carro) == 0:
        print("El carro está vacío.")
    else:
        print("Productos en el carro:")
        for producto, cantidad in carro.items():
            nombre = productos[producto]["nombre"]
            precio_unitario = productos[producto]["precio"]
            subtotal = cantidad * precio_unitario
            print(f"Producto {producto}: {nombre} - Cantidad: {cantidad} - Subtotal: {subtotal}")

def checkout():
    total = 0

    for producto, cantidad in carro.items():
        precio_unitario = productos[producto]["precio"]
        subtotal = cantidad * precio_unitario
        total += subtotal

    if set(carro.keys()) == {1, 2, 3}:
        total *= 0.8  # Aplicar descuento del 20% para productos 1, 2 y 3
    elif set(carro.keys()) == {4, 5}:
        total *= 0.85  # Aplicar descuento del 15% para productos 4 y 5

    total = round(total, 1)
    print(f"Total a pagar: USD {total}")

if __name__ == "__main__":
    while True:
        orden = input(f"Ingrese una orden \n1.agregar \n2.ver \n3.checkout\ningrese: ")

        if orden == "1":
            entrada = input("Ingrese el producto y cantidad (producto,cantidad): ")
            producto, cantidad = map(int, entrada.split(","))
            agregar_producto(producto, cantidad)
        elif orden == "2":
            mostrar_carro()
        elif orden == "3":
            checkout()
            break
        else:
            print("Orden inválida. Intente nuevamente.")