def agregar_producto(carro, producto, cantidad):
    if producto in carro:
        carro[producto] += cantidad
    else:
        carro[producto] = cantidad

def mostrar_carro(carro):
    print("Productos en el carro:")
    for producto, cantidad in carro.items():
        print("Producto {producto}: {cantidad} unidades")

def calcular_precio_descuento(carro):
    precio_total = 0
    descuento = 0

    if '1' in carro and '2' in carro and '3' in carro:
        precio_total += carro['1'] * 33.77 + carro['2'] * 203 + carro['3'] * 27.58
        descuento = 0.2
    elif '4' in carro and '5' in carro:
        precio_total += carro['4'] * 348.00 + carro['5'] * 51.19
        descuento = 0.15
    else:
        for producto, cantidad in carro.items():
            if producto == '1':
                precio_total += cantidad * 33.77
            elif producto == '2':
                precio_total += cantidad * 203
            elif producto == '3':
                precio_total += cantidad * 27.58
            elif producto == '4':
                precio_total += cantidad * 348.00
            elif producto == '5':
                precio_total += cantidad * 51.19
    
    precio_total -= precio_total * descuento
    return round(precio_total, 1)

# Diccionario para almacenar los productos en el carro
carro = {}

while True:
    orden = input("Ingrese la orden (agregar, ver, checkout): ")
    
    if orden == "agregar":
        datos = input("Ingrese el producto y la cantidad (producto,cantidad): ")
        producto, cantidad = datos.split(',')
        agregar_producto(carro, producto, int(cantidad))
    elif orden == "ver":
        mostrar_carro(carro)
    elif orden == "checkout":
        precio_total = calcular_precio_descuento(carro)
        print("Checkout:")
        mostrar_carro(carro)
        print("Precio total con descuento: ${precio_total}")
        break
    else:
        print("Orden no válida. Intente nuevamente.")
