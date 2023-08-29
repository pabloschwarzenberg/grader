# Diccionario con los productos y sus precios
productos = {
    1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203.00},
    3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}

# Carro de compras
carro = []

# Función para agregar productos al carro
def agregar_al_carro(producto_id, cantidad):
    producto_id = int(producto_id)
    cantidad = int(cantidad)
    carro.append((producto_id, cantidad))

# Función para mostrar los productos en el carro
def mostrar_carro():
    total = 0
    for producto_id, cantidad in carro:
        producto = productos[producto_id]
        nombre = producto["nombre"]
        precio = producto["precio"]
        subtotal = precio * cantidad
        total += subtotal
        print("{} (Cantidad: {}) - Subtotal: ${:.2f}".format(nombre, cantidad, subtotal))
    print("Total: ${:.2f}".format(total))

# Función para hacer el checkout y aplicar los descuentos
def checkout():
    total = 0
    for producto_id, cantidad in carro:
        producto = productos[producto_id]
        precio = producto["precio"]
        subtotal = precio * cantidad
        total += subtotal
    descuento = 0
    if (1 in [producto_id for producto_id, _ in carro] and
            2 in [producto_id for producto_id, _ in carro] and
            3 in [producto_id for producto_id, _ in carro]):
        descuento = 0.2
    elif (4 in [producto_id for producto_id, _ in carro] and
            5 in [producto_id for producto_id, _ in carro]):
        descuento = 0.15
    total_con_descuento = total - (total * descuento)
    print("Total a pagar: ${:.1f}".format(total_con_descuento))

# Ciclo principal del programa
while True:
    orden = input("Ingrese una orden (producto,cantidad / ver / checkout): ")
    if orden == "ver":
        mostrar_carro()
    elif orden == "checkout":
        checkout()
        break
    else:
        producto_id, cantidad = orden.split(",")
        agregar_al_carro(producto_id, cantidad)
