# Diccionario de productos y sus precios
productos = {
    1: ("Juego Pokemon X para Nintendo 3DS", 33.77),
    2: ("Nintendo 3DS XL", 203.00),
    3: ("Juego Mario Kart 7 para Nintendo 3DS", 27.58),
    4: ("PlayStation 4", 348.00),
    5: ("FIFA 16, PlayStation 4", 51.19)
}

# Carro de compras
carro = {}

# Función para agregar productos al carro
def agregar_al_carro(producto, cantidad):
    producto = int(producto)
    if producto in productos:
        if producto in carro:
            carro[producto] += cantidad
        else:
            carro[producto] = cantidad
        print("Se agregaron", cantidad, "unidad(es) del producto", producto)
    else:
        print("El producto", producto, "no existe.")

# Función para mostrar los productos en el carro
def ver_carro():
    print("Productos en el carro:")
    total = 0
    for producto, cantidad in carro.items():
        nombre, precio = productos[producto]
        subtotal = precio * cantidad
        print(nombre, "-", cantidad, "unidad(es) - Subtotal:", round(subtotal, 2))
        total += subtotal
    print("Total en el carro (sin descuentos):", round(total, 2))

# Función para calcular el descuento y mostrar el valor total del carro
def checkout():
    total = 0
    descuento = 0
    productos_descuento_20 = [1, 2, 3]
    productos_descuento_15 = [4, 5]
    
    for producto, cantidad in carro.items():
        nombre, precio = productos[producto]
        subtotal = precio * cantidad
        total += subtotal
        
        if set(productos_descuento_20).issubset(carro.keys()):
            descuento = total * 0.2
        elif set(productos_descuento_15).issubset(carro.keys()):
            descuento = total * 0.15

    total -= descuento
    print("Valor total del carro (con descuentos):", round(total, 1))

# Programa principal
while True:
    orden = input("Ingrese una orden (agregar, ver, checkout): ")
    if orden == "agregar":
        entrada = input("Ingrese el producto y la cantidad (producto,cantidad): ")
        producto, cantidad = entrada.split(",")
        agregar_al_carro(producto, int(cantidad))
    elif orden == "ver":
        ver_carro()
    elif orden == "checkout":
        checkout()
        break
    else:
        print("Orden no válida. Por favor, intente nuevamente.")
