# Diccionario con la información de los productos
productos = {
    1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203},
    3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}

# Diccionario para almacenar los productos en el carro
carro = {}

# Función para calcular el precio total con descuento
def calcular_precio_total():
    precio_total = 0

    # Calcular el precio total sin descuento
    for producto, cantidad in carro.items():
        precio = productos[producto]["precio"]
        precio_total += precio * cantidad

    # Aplicar descuentos
    if set(carro.keys()) == {1, 2, 3}:
        precio_total *= 0.8  # 20% de descuento
    elif set(carro.keys()) == {4, 5}:
        precio_total *= 0.85  # 15% de descuento

    return round(precio_total, 1)

# Función principal del programa
def programa_carro():
    while True:
        accion = input("Ingrese una acción (agregar, ver, checkout): ")

        if accion == "agregar":
            datos = input("Ingrese el producto y la cantidad (ejemplo: 5,2): ")
            producto, cantidad = datos.split(",")
            producto = int(producto)
            cantidad = int(cantidad)

            if producto in productos:
                if producto in carro:
                    carro[producto] += cantidad
                else:
                    carro[producto] = cantidad
                print("Producto agregado al carro.")
            else:
                print("Producto no encontrado.")

        elif accion == "ver":
            print("Productos en el carro:")
            for producto, cantidad in carro.items():
                nombre = productos[producto]["nombre"]
                precio = productos[producto]["precio"]
                print(f"{nombre} x {cantidad}: ${precio}")

        elif accion == "checkout":
            precio_total = calcular_precio_total()
            print(f"Total a pagar: ${precio_total}")
            break

        else:
            print("Acción inválida. Por favor, ingrese 'agregar', 'ver' o 'checkout'.")

# Ejecutar el programa
programa_carro()
