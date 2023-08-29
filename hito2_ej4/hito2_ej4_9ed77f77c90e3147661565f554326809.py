productos = {
    1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203},
    3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}

carro = {}

def agregar_producto(producto_id, cantidad):
    if producto_id in productos:
        if producto_id in carro:
            carro[producto_id] += cantidad
        else:
            carro[producto_id] = cantidad
        print("Producto agregado al carro.")
    else:
        print("Producto no válido.")

def ver_carro():
    print("Productos en el carro:")
    for producto_id, cantidad in carro.items():
        producto = productos[producto_id]
        nombre = producto["nombre"]
        precio = producto["precio"]
        subtotal = precio * cantidad
       print(f"Producto: {nombre} - Cantidad: {cantidad} - Subtotal: ${subtotal:.2f}")

def checkout():
    total = 0

    for producto_id, cantidad in carro.items():
        producto = productos[producto_id]
        precio = producto["precio"]
        subtotal = precio * cantidad

        if producto_id in [1, 2, 3]:
            subtotal *= 0.8
        elif producto_id in [4, 5]:
            subtotal *= 0.85

        total += subtotal

    print(f"Total a pagar: ${total:.1f}")

while True:
    accion = input("Ingrese la acción (agregar, ver, checkout): ")

    if accion == "agregar":
        entrada = input("Ingrese el producto y la cantidad (producto,cantidad): ")
        producto_id, cantidad = map(int, entrada.split(","))
        agregar_producto(producto_id, cantidad)
    elif accion == "ver":
        ver_carro()
    elif accion == "checkout":
        checkout()
        break
    else:
        print("Acción no válida. Por favor, intente nuevamente.")
