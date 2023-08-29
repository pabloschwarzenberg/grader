p1 = [1, "Pokemon X", 33.77]
p2 = [2, "Nintendo XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16", 51.19]

productos = [p1, p2, p3, p4, p5]

carro = []

def agregar_producto(producto, cantidad):
    for i in range(cantidad):
        carro.append(producto)

def ver_carro():
    for producto in carro:
        print(producto[1])

def checkout():
    total = 0
    descuento = 0
    for producto in carro:
        total += producto[2]
    if all(x in [item[0] for item in carro] for x in [1,2,3]):
        descuento += (p1[2] + p2[2] + p3[2]) * 0.2
    if all(x in [item[0] for item in carro] for x in [4,5]):
        descuento += (p4[2] + p5[2]) * 0.15
    total -= descuento
    print(round(total,1))

while True:
    entrada = input()
    if entrada == 'ver':
        ver_carro()
    elif entrada == 'checkout':
        checkout()
        break
    else:
        producto, cantidad = entrada.split(',')
        producto = int(producto)
        cantidad = int(cantidad)
        agregar_producto(productos[producto-1], cantidad)
