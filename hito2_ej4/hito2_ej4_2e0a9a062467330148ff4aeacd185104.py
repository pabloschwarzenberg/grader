productos = {
    1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203},
    3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}


descuentos = {
    "1,2,3": 0.2,
    "4,5": 0.15
}

carro = {}  

def agregar_producto(producto, cantidad):
    if producto in productos:
        if producto in carro:
            carro[producto] += cantidad
        else:
            carro[producto] = cantidad
        print("Se agregaron", cantidad, "unidades del producto", producto, "al carro.")
    else:
        print("El producto", producto, "no existe.")

def ver_carro():
    print("Productos en el carro:")
    for producto, cantidad in carro.items():
        nombre = productos[producto]["nombre"]
        precio_unitario = productos[producto]["precio"]
        subtotal = precio_unitario * cantidad
        print("Producto:", nombre, "- Cantidad:", cantidad, "- Subtotal: $", "{:.2f}".format(subtotal))

def calcular_descuento():
    total = 0.0
    for producto, cantidad in carro.items():
        precio_unitario = productos[producto]["precio"]
        subtotal = precio_unitario * cantidad
        total += subtotal
    
    descuento = 0.0
    productos_carro = sorted(carro.keys())
    productos_carro_str = ",".join(str(p) for p in productos_carro)
    if productos_carro_str in descuentos:
        descuento = descuentos[productos_carro_str]
    
    total_descuento = total - (total * descuento)
    return round(total_descuento, 1)

while True:
    orden = input("Ingrese su orden (producto,cantidad / ver / checkout): ")
    if orden == "ver":
        ver_carro()
    elif orden == "checkout":
        total_descuento = calcular_descuento()
        print("Total a pagar (con descuento): $", "{:.1f}".format(total_descuento))
        break
    else:
        try:
            producto, cantidad = map(int, orden.split(","))
            agregar_producto(producto, cantidad)
        except:
            print("Orden inválida. Por favor, ingrese una orden válida.")