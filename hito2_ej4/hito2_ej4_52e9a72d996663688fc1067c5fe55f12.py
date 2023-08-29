productos = {
    1: {"nombre": "Juego Pokemon X para Nintendo 3DS", "precio": 33.77},
    2: {"nombre": "Nintendo 3DS XL", "precio": 203},
    3: {"nombre": "Juego Mario Kart 7 para Nintendo 3DS", "precio": 27.58},
    4: {"nombre": "PlayStation 4", "precio": 348.00},
    5: {"nombre": "FIFA 16, PlayStation 4", "precio": 51.19}
}

carro = {}

def agregar_al_carro(producto, cantidad):
    if producto in productos:
        if producto in carro:
            carro[producto] += cantidad
        else:
            carro[producto] = cantidad
        print("Producto agregado al carro.")
    else:
        print("Producto no válido.")

def mostrar_carro():
    if carro:
        print("Productos en el carro:")
        for producto, cantidad in carro.items():
            nombre = productos[producto]["nombre"]
            precio = productos[producto]["precio"]
            subtotal = precio * cantidad
            print("Producto", producto, ":", nombre, cantidad, "= USD", format(subtotal, ".2f"))
    else:
        print("El carro está vacío.")

def aplicar_descuento():
    productos_carro = list(carro.keys())
    if set([1, 2, 3]).issubset(productos_carro):
        descuento = 0.2
    elif set([4, 5]).issubset(productos_carro):
        descuento = 0.15
    else:
        descuento = 0
    total = sum(productos[producto]["precio"] * cantidad for producto, cantidad in carro.items())
    total_con_descuento = total * (1 - descuento)
    return round(total_con_descuento, 1)

while True:
    orden = input("Ingrese la orden (agregar, ver, checkout): ")
    
    if orden == "agregar":
        entrada = input("Ingrese el producto y la cantidad (ejemplo: 5,2): ")
        producto, cantidad = map(int, entrada.split(","))
        agregar_al_carro(producto, cantidad)
    
    elif orden == "ver":
        mostrar_carro()
    
    elif orden == "checkout":
        total_con_descuento = aplicar_descuento()
        print("Total a pagar con descuento: USD", total_con_descuento)
        break
    
    else:
        print("Orden no válida. Inténtelo nuevamente.")
