compras = {1: 33.77, 2: 203, 3: 27.58, 4: 348, 5: 51.19}

lista = [] 
def agregar_producto(producto, cantidad):
    for i in range(cantidad):
        lista.append(producto)

def calcular_precio():
    total = sum([compras[producto] for producto in lista])
    descuento = 0
    if (1 in lista) and (2 in lista) and (3 in lista):
        descuento = total * 0.2
    elif (4 in lista) and (5 in lista):
        descuento = total * 0.15
    final = total - descuento
    return round(final, 1)

ciclo = True
while ciclo:
    orden = input()
    if orden == "checkout":
        print("El precio total es: USD", calcular_precio())
        ciclo = False
    elif orden == "ver":
        print("Los productos en el carro son:", lista)
    else:
        orden = orden.split(",")
        producto = int(orden[0])
        cantidad = int(orden[1])
        agregar_producto(producto, cantidad)