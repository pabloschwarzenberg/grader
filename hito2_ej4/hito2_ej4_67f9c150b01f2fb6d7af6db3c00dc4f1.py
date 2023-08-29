p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
productos = {1: 33.77, 2: 203, 3: 27.58, 4: 348, 5: 51.19}


carro = [] 
def agregar_producto(producto, cantidad):
    for i in range(cantidad):
        carro.append(producto)

def calcular_precio():
    precio_total = sum([productos[producto] for producto in carro])
    descuento = 0
    if (1 in carro) and (2 in carro) and (3 in carro):
        descuento = precio_total * 0.2
    elif (4 in carro) and (5 in carro):
        descuento = precio_total * 0.15
    precio_final = precio_total - descuento
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