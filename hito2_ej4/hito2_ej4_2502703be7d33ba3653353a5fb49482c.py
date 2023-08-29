productos = {
    1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203.00},
    3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}

carro = []
total = 0.0

def agregar_producto(producto_id, cantidad):
    producto_id = int(producto_id)
    cantidad = int(cantidad)

    if producto_id not in productos:
        print("El producto no existe.")
        return

    producto = productos[producto_id]
    subtotal = producto["precio"] * cantidad
    carro.append((producto["nombre"], cantidad, subtotal))

    print(f"Se agregaron {cantidad} unidades de {producto['nombre']} al carro.")

def imprimir_carro():
    if not carro:
        print("El carro está vacío.")
        return

    print("Productos en el carro:")
    for producto in carro:
        nombre = producto[0]
        cantidad = producto[1]
        subtotal = producto[2]
        print(f"{nombre} - Cantidad: {cantidad} - Subtotal: ${subtotal:.2f}")

def calcular_descuento():
    global total
    total = sum(producto[2] for producto in carro)

    if len(carro) >= 3 and all(producto[0] in [1, 2, 3] for producto in carro):
        descuento = total * 0.2
    elif len(carro) >= 2 and all(producto[0] in [4, 5] for producto in carro):
        descuento = total * 0.15
    else:
        descuento = 0.0

    total -= descuento

def realizar_checkout():
    calcular_descuento()
    print(f"Total a pagar: ${total:.1f}")
    print("Gracias por su compra.")

if __name__ == "__main__":
    while True:
        orden = input("Ingrese la orden (producto,cantidad / ver / checkout): ")
        if orden == "ver":
            imprimir_carro()
        elif orden == "checkout":
            realizar_checkout()
            break
        else:
            producto_id, cantidad = orden.split(",")
            agregar_producto(producto_id, cantidad)
