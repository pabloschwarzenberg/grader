p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
 # Diccionario con los productos y sus precios
productos = {
    1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203},
    3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}

# Diccionario con los descuentos por combinación de productos
descuentos = {
    (1, 2, 3): 0.2,
    (4, 5): 0.15
}

carro = {}

def agregar_producto(producto, cantidad):
    producto = int(producto)
    if producto in productos:
        if producto in carro:
            carro[producto] += cantidad
        else:
            carro[producto] = cantidad
        print(f"Se agregaron {cantidad} unidades del producto {producto} al carro.")
    else:
        print("Producto no válido.")

def ver_productos():
    if carro:
        print("Productos en el carro:")
        for producto, cantidad in carro.items():
            nombre = productos[producto]["nombre"]
            precio = productos[producto]["precio"]
            print(f"Producto {producto}: {nombre} - Cantidad: {cantidad} - Precio unitario: ${precio}")
    else:
        print("El carro está vacío.")

def checkout():
    total = 0.0
    descuento_aplicado = False

    # Calcular el valor total sin descuentos
    for producto, cantidad in carro.items():
        precio = productos[producto]["precio"]
        total += precio * cantidad

    # Aplicar descuentos
    for combo, descuento in descuentos.items():
        if all(producto in carro for producto in combo):
            descuento_aplicado = True
            total *= (1 - descuento)

    # Imprimir el valor total considerando descuentos
    if descuento_aplicado:
        total = round(total, 1)
        print(f"El total a pagar con descuentos es: ${total}")
    else:
        print("No se aplicaron descuentos. El total a pagar es: ${total}")

if __name__ == "__main__":
    while True:
        orden = input("Ingrese su orden (producto,cantidad / ver / checkout): ")

        if orden == "ver":
            ver_productos()
        elif orden == "checkout":
            checkout()
            break
        else:
            producto, cantidad = orden.split(",")
            agregar_producto(producto, int(cantidad))
     