p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

# Precios de los productos
precios = {
    1: p1[2],
    2: p2[2],
    3: p3[2],
    4: p4[2],
    5: p5[2]
}

# Descuentos por combinación de productos
descuentos = {
    (1, 2, 3): 0.2,
    (4, 5): 0.15
}

# Carro de compras
carro = {}

# Función para agregar productos al carro
def agregar_producto(producto, cantidad):
    producto = int(producto)
    cantidad = int(cantidad)
    
    if producto in carro:
        carro[producto] += cantidad
    else:
        carro[producto] = cantidad

# Función para imprimir los productos en el carro
def imprimir_productos():
    for producto, cantidad in carro.items():
        if producto == 1:
            print(f"Producto {p1[0]}: {p1[1]} - Cantidad {cantidad}")
        elif producto == 2:
            print(f"Producto {p2[0]}: {p2[1]} - Cantidad {cantidad}")
        elif producto == 3:
            print(f"Producto {p3[0]}: {p3[1]} - Cantidad {cantidad}")
        elif producto == 4:
            print(f"Producto {p4[0]}: {p4[1]} - Cantidad {cantidad}")
        elif producto == 5:
            print(f"Producto {p5[0]}: {p5[1]} - Cantidad {cantidad}")

# Función para calcular el precio total con descuentos
def calcular_precio_total():
    precio_total = 0
    
    for producto, cantidad in carro.items():
        precio_total += precios[producto] * cantidad
        
    for productos_descuento, descuento in descuentos.items():
        if all(producto in carro for producto in productos_descuento):
            precio_descuento = sum(precios[producto] * carro[producto] for producto in productos_descuento)
            descuento_total = precio_descuento * descuento
            precio_total -= descuento_total
    
    return round(precio_total, 1)

# Solicitar acciones al usuario
while True:
    accion = input("Ingrese una acción (agregar, ver, checkout): ")
    
    if accion == "agregar":
        producto, cantidad = input("Ingrese el producto y la cantidad (producto,cantidad): ").split(",")
        agregar_producto(producto, cantidad)
    elif accion == "ver":
        imprimir_productos()
    elif accion == "checkout":
        precio_total = calcular_precio_total()
        print("El precio total es:", precio_total)
        break
    else:
        print("Acción inválida. Intente nuevamente.")
