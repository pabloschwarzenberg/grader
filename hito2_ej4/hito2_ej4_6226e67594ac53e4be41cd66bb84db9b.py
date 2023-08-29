def agregar_producto(carro, producto):
    carro.append(producto)

def mostrar_carro(carro):
    print("Productos en el carro:")
    for producto in carro:
        print(producto)

def calcular_precio(productos):
    precio_total = 0

    cantidades = {}
    for producto in productos:
        prod_id, cantidad = producto.split(",")
        if prod_id in cantidades:
            cantidades[prod_id] += int(cantidad)
        else:
            cantidades[prod_id] = int(cantidad)

    for prod_id, cantidad in cantidades.items():
        if prod_id == '1' or prod_id == '2' or prod_id == '3':
            if cantidad >= 3:
                precio_total += (cantidad * get_precio(prod_id)) * 0.8
            else:
                precio_total += cantidad * get_precio(prod_id)
        else:
            precio_total += cantidad * get_precio(prod_id)

    return round(precio_total, 1)

def get_precio(prod_id):
    if prod_id == '1':
        return 33.77
    elif prod_id == '2':
        return 203
    elif prod_id == '3':
        return 27.58
    elif prod_id == '4':
        return 348
    elif prod_id == '5':
        return 51.19
    else:
        return 0

carro = []

while True:
    orden = input("Ingrese una orden (producto,cantidad / ver / checkout): ")

    if orden == "ver":
        mostrar_carro(carro)
    elif orden == "checkout":
        precio_total = calcular_precio(carro)
        print("El precio total es:", precio_total)
        break
    else:
        agregar_producto(carro, orden)
