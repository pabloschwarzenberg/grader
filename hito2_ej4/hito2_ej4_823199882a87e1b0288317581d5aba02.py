# Diccionario de productos
productos = {
    1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203},
    3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}

# Variables para almacenar los productos en el carro
carro = {}
descuento = 0

# Función para agregar productos al carro
def agregar_producto(producto, cantidad):
    if producto in productos:
        if producto in carro:
            carro[producto] += cantidad
        else:
            carro[producto] = cantidad
        print("Producto "+str(producto)+" agregado al carro.")
    else:
        print("No se encontró el producto "+str(producto))

# Función para mostrar los productos en el carro
def ver_carro():
    if len(carro) > 0:
        print("Productos en el carro:")
        for producto, cantidad in carro.items():
            nombre_producto = productos[producto]["nombre"]
            print("Producto: "+nombre_producto+" - Cantidad: {cantidad}")
    else:
        print("El carro está vacío.")

# Función para calcular el total a pagar
def calcular_total():
    total = 0

    # Calcular el valor total sin descuento
    for producto, cantidad in carro.items():
        precio = productos[producto]["precio"]
        total += precio * cantidad

    # Aplicar descuentos si corresponde
    if set([1, 2, 3]).issubset(carro):
        global descuento
        descuento = total * 0.2

    if set([4, 5]).issubset(carro):
        descuento = total * 0.15

    total -= descuento
    return round(total, 1)

# Loop principal del programa
while True:
    orden = input("Ingrese una orden (producto, ver, checkout): ")

    if orden == "ver":
        ver_carro()

    elif orden == "checkout":
        total = calcular_total()
        print(str(total))
        break

    else:
        entrada = orden
        producto, cantidad = map(int, entrada.split(","))
        agregar_producto(producto, cantidad)
