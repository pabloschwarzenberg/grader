productos = {
    1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203},
    3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}

carro = {}

def agregar_producto(producto_id, cantidad):
    producto_id = int(producto_id)
    cantidad = int(cantidad)
    
    if producto_id in productos:
        if producto_id in carro:
            carro[producto_id] += cantidad
        else:
            carro[producto_id] = cantidad
        print(f"Se agregaron {cantidad} unidad(es) del producto {producto_id}.")
    else:
        print("El producto ingresado no existe.")

def ver_productos():
    print("Productos en el carro:")
    for producto_id, cantidad in carro.items():
        producto = productos[producto_id]
        nombre = producto["nombre"]
        precio = producto["precio"]
        subtotal = precio * cantidad
        print(f"{nombre} (Cantidad: {cantidad}) - Subtotal: ${subtotal:.2f}")

def calcular_total():
    total = 0
    descuento = 0
    
    productos_agregados = carro.keys()
    
    if {1, 2, 3}.issubset(productos_agregados):
        descuento = 0.2
    elif {4, 5}.issubset(productos_agregados):
        descuento = 0.15
    
    for producto_id, cantidad in carro.items():
        producto = productos[producto_id]
        precio = producto["precio"]
        subtotal = precio * cantidad
        total += subtotal
    
    total -= total * descuento
    total = round(total, 1)
    
    print(f"Total a pagar: ${total:.1f}")

if __name__ == "__main__":
    while True:
        accion = input("Ingrese una acción (agregar, ver, checkout): ")
        
        if accion == "agregar":
            entrada = input("Ingrese el producto y cantidad (producto,cantidad): ")
            producto_id, cantidad = entrada.split(",")
            agregar_producto(producto_id, cantidad)
        elif accion == "ver":
            ver_productos()
        elif accion == "checkout":
            calcular_total()
            break
        else:
            print("Acción no válida. Intente nuevamente.")
