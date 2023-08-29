productos = {
    1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203},
    3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}

carro = {}

def agregar_producto(producto_id, cantidad):
    if producto_id in carro:
        carro[producto_id] += cantidad
    else:
        carro[producto_id] = cantidad

def ver_carro():
    for producto_id in carro:
        producto = productos[producto_id]
        print("producto",'nombre',carro[producto_id]")

def checkout():
    total = 0
    for producto_id in carro:
        producto = productos[producto_id]
        precio = producto["precio"]
        cantidad = carro[producto_id]
        if producto_id in [1,2,3]:
            precio *= (1 - 0.2)
        elif producto_id in [4,5]:
            precio *= (1 - 0.15)
        total += precio * cantidad
    print("Total:",round(total,1)")
