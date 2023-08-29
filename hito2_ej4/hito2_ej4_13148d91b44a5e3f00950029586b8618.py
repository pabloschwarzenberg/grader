# Diccionario de productos
productos = {
    1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203},
    3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}

# Variables de carro y descuentos
carro = {}
descuento1 = 0.20  # Descuento del 20% para productos 1, 2 y 3
descuento2 = 0.15  # Descuento del 15% para productos 4 y 5

# Función para agregar productos al carro
def agregar_producto(producto, cantidad):
    if producto in carro:
        carro[producto] += cantidad
    else:
        carro[producto] = cantidad

# Función para mostrar los productos en el carro
def mostrar_carro():
    print("Productos en el carro:")
    for producto, cantidad in carro.items():
        nombre = productos[producto]["nombre"]
        precio = productos[producto]["precio"]
        subtotal = cantidad * precio
        print(f"{nombre} x {cantidad}: ${subtotal:.1f}")

# Función para realizar el checkout
def checkout():
    total = 0
    for producto, cantidad in carro.items():
        precio = productos[producto]["precio"]
        subtotal = cantidad * precio
        total += subtotal

    if 1 in carro and 2 in carro and 3 in carro:
        total *= (1 - descuento1)
    elif 4 in carro and 5 in carro:
        total *= (1 - descuento2)

    print(f"Total a pagar: ${total:.1f}")

# Programa principal
while True:
    orden = input("Ingrese una orden (agregar, ver, checkout): ")

    if orden == "agregar":
        datos = input("Ingrese el producto y la cantidad (producto,cantidad): ")
        producto, cantidad = map(int, datos.split(","))
        agregar_producto(producto, cantidad)
    elif orden == "ver":
        mostrar_carro()
    elif orden == "checkout":
        checkout()
        break
    else:
        print("Orden no válida. Intente nuevamente.")

      