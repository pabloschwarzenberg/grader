def descuentos(carrito_de_compras):
    if all(carrito_de_compras.count(j)>=1 for j in [1,2,3]):
        if all(carrito_de_compras.count(l)>=1 for l in [4,5]):
            return 3 #ambos descuentos
        else:
            return 1 #solo descuento 1
    else:
        if all(carrito_de_compras.count(l) >= 1 for l in [4, 5]):
            return 2 #solo descuento 2
        else:
            return 0 #ninguno descuento


p1 = [1, "Pokemon X", 33.77]
p2 = [2, "Nintendo XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16", 51.19]
catalogo = [p1, p2, p3, p4, p5]
carrito_de_compras = []
operacion = input()
total = 0
while operacion != 'checkout':
    if operacion == 'ver':
        for i in catalogo:
            print(i[1])
    else:
        operacion = operacion.split(',')
        for i in range(int(operacion[1])):
            carrito_de_compras.append(int(operacion[0]))
    operacion = input()
if descuentos(carrito_de_compras) == 3:
    total_parcial = 0
    for producto in carrito_de_compras:
        if producto in [1,2,5]:
            total_parcial += catalogo[carrito_de_compras.pop(carrito_de_compras.index(producto)) -1][2]
    total += total_parcial*0.8
    total_parcial = 0
    for producto in carrito_de_compras:
        if producto in [4,5]:
            total_parcial += catalogo[carrito_de_compras.pop(carrito_de_compras.index(producto)) - 1][2]
    total += total_parcial*0.85

elif descuentos(carrito_de_compras) == 2:
    total_parcial = 0
    for producto in carrito_de_compras:
        if producto in [4,5]:
            total_parcial += catalogo[carrito_de_compras.pop(carrito_de_compras.index(producto)) - 1][2]
    total += total_parcial*0.85
elif descuentos(carrito_de_compras) == 1:
    total_parcial = 0
    for producto in carrito_de_compras:
        if producto in [1,2,5]:
            total_parcial += catalogo[carrito_de_compras.pop(carrito_de_compras.index(producto)) -1][2]
    total += total_parcial*0.8
for producto in carrito_de_compras:
    total += catalogo[producto-1][2]
total = round(total, 1)
print(total)
