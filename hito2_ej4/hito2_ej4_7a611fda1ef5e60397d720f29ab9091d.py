# Diccionario de productos y sus precios
productos = {
    1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203},
    3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}

# Carro de compras
carro = {}

def agregar_producto(orden):
    # Obtener los detalles del producto y la cantidad de la orden
    producto_id, cantidad = map(int, orden.split(","))
    
    if producto_id in productos:
        if producto_id in carro:
            carro[producto_id] += cantidad
        else:
            carro[producto_id] = cantidad
        print(f"Se agregaron {cantidad} unidades del producto {producto_id} al carro.")
    else:
        print("El producto no existe.")

def mostrar_productos():
    print("Productos en el carro:")
    for producto_id, cantidad in carro.items():
        producto = productos[producto_id]
        nombre = producto["nombre"]
        precio = producto["precio"]
        print(f"{nombre} (Cantidad: {cantidad}) - Precio unitario: ${precio:.2f}")

def hacer_checkout():
    total = 0
    
    for producto_id, cantidad in carro.items():
        producto = productos[producto_id]
        precio = producto["precio"]
        
        if producto_id in [1, 2, 3] and len(carro) >= 3:
            # Aplicar descuento del 20% si se agregaron productos 1, 2 y 3 al carro
            descuento = 0.2
        elif producto_id in [4, 5] and len(carro) >= 2:
            # Aplicar descuento del 15% si se agregaron productos 4 y 5 al carro
            descuento = 0.15
        else:
            descuento = 0
        
        subtotal = precio * cantidad
        descuento_aplicado = subtotal * descuento
        total += subtotal - descuento_aplicado
    
    print(f"Total a pagar: ${round(total, 1)}")

# Ejecución del programa
while True:
    orden = input("Ingrese una orden (agregar, ver, checkout): ")
    
    if orden.startswith("agregar"):
        agregar_producto(orden.split(" ")[1])
    elif orden == "ver":
        mostrar_productos()
    elif orden == "checkout":
        hacer_checkout()
        break
    else:
        print("Orden no válida. Por favor, ingrese 'agregar', 'ver' o 'checkout'.")
