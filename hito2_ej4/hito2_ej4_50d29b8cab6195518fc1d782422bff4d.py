# Diccionario con los productos y sus precios
productos = {
    1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203},
    3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}

# Variables para almacenar los productos en el carro
carro = {}
descuento_total = 0

def agregar_producto(producto, cantidad):
    global carro
    if producto in productos:
        if producto in carro:
            carro[producto] += cantidad
        else:
            carro[producto] = cantidad
        print("Se agregaron {cantidad} unidades del producto {producto} al carro.")
    else:
        print("El producto ingresado no existe.")

def mostrar_carro():
    global carro
    for producto, cantidad in carro.items():
        nombre = productos[producto]["nombre"]
        precio_unitario = productos[producto]["precio"]
        subtotal = precio_unitario * cantidad
        print(f"Producto: {nombre}\nCantidad: {cantidad}\nPrecio Unitario: ${precio_unitario}\nSubtotal: ${subtotal}\n")

def checkout():
    global carro, descuento_total
    total = 0
    for producto, cantidad in carro.items():
        precio_unitario = productos[producto]["precio"]
        subtotal = precio_unitario * cantidad
        total += subtotal
    
    if len(carro) >= 3 and all(producto in carro for producto in [1, 2, 3]):
        descuento = total * 0.2
        descuento_total += descuento
    elif len(carro) >= 2 and all(producto in carro for producto in [4, 5]):
        descuento = total * 0.15
        descuento_total += descuento
    
    total -= descuento_total

    print(f"Valor total de los productos en el carro (con descuento): ${round(total, 1)}")

# Función principal del programa
def main():
    while True:
        orden = input("Ingrese una orden (producto,cantidad / ver / checkout): ")

        if orden == "ver":
            mostrar_carro()
        elif orden == "checkout":
            checkout()
            break
        else:
            try:
                producto, cantidad = map(int, orden.split(","))
                agregar_producto(producto, cantidad)
            except:
                print("Orden inválida. Por favor, ingrese una orden válida.")

# Ejecutar el programa
if __name__ == "__main__":
    main()


      