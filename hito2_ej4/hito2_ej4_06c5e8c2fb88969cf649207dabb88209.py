# Diccionario de productos y sus precios
productos = {
    1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203.00},
    3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}

# Carro de compras
carro = []

def agregar_producto(producto_id, cantidad):
    producto_id = int(producto_id)
    cantidad = int(cantidad)

    # Verificar si el producto existe en el diccionario
    if producto_id not in productos:
        print("El producto seleccionado no existe.")
        return

    # Agregar el producto al carro
    producto = productos[producto_id]
    carro.append({"producto_id": producto_id, "nombre": producto["nombre"], "precio": producto["precio"], "cantidad": cantidad})
    print(f"Se agregaron {cantidad} unidad(es) de {producto['nombre']} al carro.")

def mostrar_productos():
    if not carro:
        print("El carro está vacío.")
        return

    print("Productos en el carro:")
    for item in carro:
        producto_id = item["producto_id"]
        nombre = item["nombre"]
        precio = item["precio"]
        cantidad = item["cantidad"]
        print(f"Producto ID: {producto_id}, Nombre: {nombre}, Precio: {precio}, Cantidad: {cantidad}")

def calcular_total():
    total = 0.0

    # Calcular el total sin descuentos
    for item in carro:
        precio = item["precio"]
        cantidad = item["cantidad"]
        subtotal = precio * cantidad
        total += subtotal

    # Aplicar descuentos según los productos en el carro
    descuento = 0.0
    productos_en_carro = [item["producto_id"] for item in carro]

    if set([1, 2, 3]).issubset(productos_en_carro):
        descuento = total * 0.20
    elif set([4, 5]).issubset(productos_en_carro):
        descuento = total * 0.15

    total -= descuento
    total = round(total, 1)
    return total

# Programa principal
while True:
    orden = input("Ingrese una orden (agregar, ver, checkout): ")

    if orden == "agregar":
        producto_id, cantidad = input("Ingrese el producto y la cantidad (producto,cantidad): ").split(",")
        agregar_producto(producto_id, cantidad)
    elif orden == "ver":
        mostrar_productos()
    elif orden == "checkout":
        total = calcular_total()
        print(f"Total a pagar: ${total}")
        break
    else:
        print("Orden inválida. Intente nuevamente.")