productos = {1: 33.77, 2: 203, 3: 27.58, 4: 348, 5: 51.19}


carro = [] 
def agregar_producto(producto, cantidad):
    for i in range(cantidad):
        carro.append(producto)

def calcular_precio():
    p_total = sum([productos[producto] for producto in carro])
    descuento = 0
    if (1 in carro) and (2 in carro) and (3 in carro):
        t_descuento = p_total * 0.2
    elif (4 in carro) and (5 in carro):
        t_descuento = p_total * 0.15
    precio_final = p_total - t_descuento
    return round(precio_final, 1)

while True:
    orden = input()
    if orden == "checkout":
        print("El precio total es: USD", calcular_precio())
        break
    elif orden == "ver":
        print("Los productos en el carro son:", carro)
    else:
        orden = orden.split(",")
        producto = int(orden[0])
        cantidad = int(orden[1])
        agregar_producto(producto, cantidad)
        
      