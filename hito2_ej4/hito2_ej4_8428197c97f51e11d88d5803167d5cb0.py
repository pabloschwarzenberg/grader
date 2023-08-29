Definimos un diccionario con los productos y sus precios
productos = {
    1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203.00},
    3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19},
}

# Definimos un diccionario con los descuentos
descuentos = {
    "set1": {"productos": [1, 2, 3], "descuento": 0.2},
    "set2": {"productos": [4, 5], "descuento": 0.15},
}

# Inicializamos el carro como un diccionario vacío
carro = {}

# Función que agrega productos al carro
def agregar_producto(producto, cantidad):
    if producto in productos:
        if producto in carro:
            carro[producto] += cantidad
        else:
            carro[producto] = cantidad
        print(f"Producto agregado al carro: {productos[producto]['nombre']} x{cantidad}")
    else:
        print("Producto no válido")

# Función que muestra los productos en el carro
def mostrar_carro():
    if carro:
        print("Productos en el carro:")
        total = 0
        for producto, cantidad in carro.items():
            nombre = productos[producto]['nombre']
            precio = productos[producto]['precio']
            subtotal = cantidad * precio
            print(f"- {nombre} (USD {precio:.2f}) x{cantidad}")
            total += subtotal
        print(f"Total a pagar: USD {total:.2f}")
    else:
        print("El carro está vacío")

# Función que calcula el descuento a aplicar
def calcular_descuento():
    # Obtener los productos en el carro como una lista
    productos_carro = list(carro.keys())
    # Comprobar si se cumple el descuento 1
    if all(p in productos_carro for p in descuentos['set1']['productos']):
        descuento = descuentos['set1']['descuento']
    # Comprobar si se cumple el descuento 2
    elif all(p in productos_carro for p in descuentos['set2']['productos']):
        descuento = descuentos['set2']['descuento']
    else:
        descuento = 0
    return descuento

# Función que hace el checkout
def hacer_checkout():
    if carro:
        descuento = calcular_descuento()
        total = 0
        for producto, cantidad in carro.items():
            precio = productos[producto]['precio']
            subtotal = cantidad * precio
            total += subtotal
        descuento_aplicado = total * descuento
        total_con_descuento = total - descuento_aplicado
        print(f"Total a pagar: USD {total_con_descuento:.2f} (Descuento aplicado: {descuento_aplicado * 100:.0f}%)")
        # Reiniciamos el carro después del checkout
        carro.clear()
    else:
        print("El carro está vacío")

# Programa principal
while True:
    accion = input("> ")
    if accion == "ver":
        mostrar_carro()
    elif accion == "checkout":
        hacer_checkout()
    else:
        try:
            producto, cantidad = accion.split(",")
            agregar_producto(int(producto), int(cantidad))
        except:
            print("Entrada inválida")    