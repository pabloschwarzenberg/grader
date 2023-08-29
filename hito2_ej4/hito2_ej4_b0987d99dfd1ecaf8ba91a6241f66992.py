productos = {
    1: {"nombre": "Pokemon X", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203},
    3: {"nombre": "Mario Kart 7", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16 - PlayStation 4", "precio": 51.19}
}

carro = []

def agregar_producto(producto, cantidad):
    carro.append((producto, cantidad))
    print("Producto agregado al carro.")

def mostrar_productos():
    if not carro:
        print("El carro de compras está vacío.")
    else:
        print("Productos en el carro:")
        for item in carro:
            producto = productos[item[0]]
            nombre = producto["nombre"]
            precio = producto["precio"]
            cantidad = item[1]
            print(f"{nombre} - Cantidad: {cantidad} - Precio unitario: ${precio:.2f}")

def realizar_checkout():
    total = 0
    descuento = 0
    
    for item in carro:
        producto = productos[item[0]]
        precio = producto["precio"]
        cantidad = item[1]
        subtotal = precio * cantidad
        total += subtotal
        
        if item[0] in [1, 2, 3]:
            descuento += subtotal * 0.20
        
        if item[0] in [4, 5]:
            descuento += subtotal * 0.15
    
    total -= descuento
    
    print(f"Total a pagar: ${total:.1f}")
    
while True:
    accion = input("Ingrese la acción a realizar (agregar, ver, checkout): ")
    
    if accion == "agregar":
        producto, cantidad = map(int, input("Ingrese el producto y la cantidad (producto,cantidad): ").split(","))
        if producto in productos:
            agregar_producto(producto, cantidad)
        else:
            print("Producto no válido. Intente nuevamente.")
    
    elif accion == "ver":
        mostrar_productos()
    
    elif accion == "checkout":
        realizar_checkout()
        break
    
    else:
        print("Acción no válida. Intente nuevamente.")
