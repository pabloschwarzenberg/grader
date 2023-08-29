productos = {
    1: ["Pokemon X para Nintendo 3DS", 33.77],
    2: ["Nintendo 3DS XL", 203],
    3: ["Mario Kart 7 para Nintendo 3DS", 27.58],
    4: ["PlayStation 4", 348.00],
    5: ["FIFA 16, PlayStation 4", 51.19]
carro = []
def agregar_producto(producto, cantidad):
    producto_id = int(producto)
    if producto_id in productos:
        carro.append((producto_id, cantidad))
        print(f"Se agregaron {cantidad} unidades del producto {producto_id} al carro.")
    else:
        print("Producto no válido.")

def mostrar_productos():
    if len(carro) == 0:
        print("El carro está vacío.")
    else:
        print("Productos en el carro:")
        total = 0
        for producto_id, cantidad in carro:
            nombre = productos[producto_id][0]
            precio = productos[producto_id][1]
            subtotal = precio * cantidad
            print(f"{nombre} x {cantidad}: USD {subtotal:.2f}")
            total += subtotal
        print(f"Total a pagar: USD {total:.2f}")

def checkout():
    descuento = 0
    for producto_id, cantidad in carro:
        if producto_id in [1, 2, 3]:
            descuento += 0.2
        elif producto_id in [4, 5]:
            descuento += 0.15

    total = 0
    for producto_id, cantidad in carro:
        precio = productos[producto_id][1]
        subtotal = precio * cantidad
        total += subtotal

    total_descuento = total * (1 - descuento)
    print(f"Total a pagar con descuento: USD {total_descuento:.1f}")

while True:
    orden = input("Ingrese una orden (agregar, ver, checkout): ")
    
    if orden == "agregar":
        entrada = input("Ingrese el producto y la cantidad (producto,cantidad): ")
        producto, cantidad = entrada.split(",")
        agregar_producto(producto, int(cantidad))
    elif orden == "ver":
        mostrar_productos()
    elif orden == "checkout":
        checkout()
        break
    else:
        print("Orden no válida. Por favor, intente nuevamente.")
