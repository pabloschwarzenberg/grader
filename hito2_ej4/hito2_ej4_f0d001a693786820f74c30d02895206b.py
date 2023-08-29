# Definimos el diccionario de productos con su información
productos = {
    "1": {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    "2": {"nombre": "Nintendo 3DS XL", "precio": 203},
    "3": {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    "4": {"nombre": "PlayStation 4", "precio": 348.00},
    "5": {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
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
        print("El producto no existe.")


def mostrar_carro():
    print("Productos en el carro:")
    for producto, cantidad in carro.items():
        nombre = productos[producto]["nombre"]
        precio = productos[producto]["precio"]
        subtotal = cantidad * precio
        print(f"{nombre} (Cantidad: {cantidad}) - Subtotal: ${subtotal}")

# Función para hacer el checkout y calcular el valor total con descuento
def checkout():
    total = 0
    for producto, cantidad in carro.items():
        precio = productos[producto]["precio"]
        subtotal = cantidad * precio
        total += subtotal

    if "1" in carro and "2" in carro and "3" in carro:
        total *= 0.8  # Aplicar descuento del 20%
    elif "4" in carro and "5" in carro:
        total *= 0.85  # Aplicar descuento del 15%

    total = round(total, 1)
    print(f"Total a pagar: ${total}")

# Programa principal
while True:
    orden = input("Ingrese la orden (agregar, ver, checkout): ")

    if orden == "agregar":
        datos = input("Ingrese el producto y la cantidad (producto,cantidad): ")
        producto, cantidad = datos.split(",")
        agregar_producto(producto, int(cantidad))

    elif orden == "ver":
        mostrar_carro()

    elif orden == "checkout":
        checkout()
        break

    else:
        print("Orden inválida. Intente nuevamente.")