# Diccionario de productos
productos = {
    1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203},
    3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}

carro = {}  # Carro de compras

# Función para agregar productos al carro
def agregar_producto(numero, cantidad):
    if numero in productos:
        if numero in carro:
            carro[numero] += cantidad
        else:
            carro[numero] = cantidad
        print(f"Se agregaron {cantidad} unidades del producto {numero} al carro.")
    else:
        print("El número de producto no es válido.")

# Función para mostrar los productos en el carro
def ver_productos():
    print("Productos en el carro:")
    for numero, cantidad in carro.items():
        producto = productos[numero]
        nombre = producto["nombre"]
        print(f"{numero}: {nombre} x {cantidad}")

# Función para calcular el total a pagar con descuentos
def calcular_total():
    total = 0
    descuento = 0
    
    # Descuento del 20% si los productos 1, 2 y 3 están en el carro
    if all(numero in carro for numero in [1, 2, 3]):
        total_descuento = sum(productos[numero]["precio"] * carro[numero] for numero in [1, 2, 3])
        descuento = total_descuento * 0.2
    
    # Descuento del 15% si los productos 4 y 5 están en el carro
    if all(numero in carro for numero in [4, 5]):
        total_descuento = sum(productos[numero]["precio"] * carro[numero] for numero in [4, 5])
        descuento = max(descuento, total_descuento * 0.15)
    
    # Cálculo del total a pagar
    total = sum(productos[numero]["precio"] * carro[numero] for numero in carro)
    total -= descuento
    
    return round(total, 1)

# Programa principal
while True:
    orden = input("Ingrese una orden (agregar, ver, checkout): ")
    
    if orden == "agregar":
        entrada = input("Ingrese el número del producto y la cantidad (producto,cantidad): ")
        numero, cantidad = entrada.split(",")
        agregar_producto(int(numero), int(cantidad))
    
    elif orden == "ver":
        ver_productos()
    
    elif orden == "checkout":
        total = calcular_total()
        print(f"Total a pagar: {total}")
        break
    
    else:
        print("Orden no válida. Intente nuevamente.")
