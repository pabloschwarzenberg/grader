# Diccionario con la información de los productos
productos = {
    1: {'nombre': 'Juego Pokemon X para Nintendo 3DS', 'precio': 33.77},
    2: {'nombre': 'Nintendo 3DS XL', 'precio': 203},
    3: {'nombre': 'Juego Mario Kart 7 para Nintendo 3DS', 'precio': 27.58},
    4: {'nombre': 'PlayStation 4', 'precio': 348.00},
    5: {'nombre': 'FIFA 16, PlayStation 4', 'precio': 51.19}
}

# Variables para el carro de compras y el total
carro = {}
total = 0.0

# Función para agregar productos al carro
def agregar_producto(producto, cantidad):
    global total
    
    if producto in productos:
        precio = productos[producto]['precio']
        subtotal = precio * cantidad
        
        if producto in carro:
            carro[producto] += cantidad
        else:
            carro[producto] = cantidad
        
        total += subtotal
        
        print("Se agregaron {} unidades del producto {} al carro.".format(cantidad, producto))
    else:
        print("Producto no válido.")

# Función para mostrar los productos en el carro
def ver_carro():
    print("Productos en el carro:")
    
    for producto, cantidad in carro.items():
        nombre = productos[producto]['nombre']
        subtotal = productos[producto]['precio'] * cantidad
        print("{}: {} (Cantidad: {}, Subtotal: {:.1f})".format(producto, nombre, cantidad, subtotal))
    
    print("Total: {:.1f}".format(total))

# Función para hacer el checkout
def checkout():
    if len(carro) == 0:
        print("El carro está vacío.")
    else:
        descuento = 0.0
        
        if all(p in carro for p in [1, 2, 3]):
            descuento = total * 0.2
        elif all(p in carro for p in [4, 5]):
            descuento = total * 0.15
        
        total_descuento = total - descuento
        
        print("Total a pagar (con descuento): {:.1f}".format(total_descuento))
        
        # Reiniciar el carro y el total
        carro.clear()
        total = 0.0

# Función principal
def main():
    while True:
        orden = input("Ingrese su orden (agregar, ver, checkout), o 'salir' para terminar: ")
        
        if orden == "agregar":
            entrada = input("Ingrese el producto y la cantidad (producto,cantidad): ")
            producto, cantidad = map(int, entrada.split(","))
            agregar_producto(producto, cantidad)
        elif orden == "ver":
            ver_carro()
        elif orden == "checkout":
            checkout()
        elif orden == "salir":
            break
        else:
            print("Orden no válida.")

if __name__ == "__main__":
    main()