def comprasAmazon(pedido, p1, p2, p3, p4, p5):
    total = 0
    oferta = []
    for compra in pedido:
        if p1[0] == compra[0]:
            total += (p1[2])*int(compra[-1])
            oferta.append("p1")
        elif p2[0] == compra[0]:
            total += (p2[2])*int(compra[-1])
            oferta.append("p2")
        elif p3[0] == compra[0]:
            total += (p3[2])*int(compra[-1])
            oferta.append("p3")
        elif p4[0] == compra[0]:
            total += (p4[2])*int(compra[-1])
            oferta.append("p4")
        elif p5[0] == compra[0]:
            total += (p5[2])*int(compra[-1])
            oferta.append("p5")
    if ["p1", "p2", "p3"] in oferta:
        total -= (total * .2)
    if ["p4", "p5"] in oferta:
        total -= (total * .15)
    return total


p1 = [1, "Pokemon X", 33.77]
p2 = [2, "Nintendo XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16", 51.19]

lista = []
while True:
    pedido = input("Ingrese pedido y cantidad: ")
    if pedido == "checkout":
        break
    elif pedido == "ver":
        print(lista)
    else:
        lista.append(pedido)
print(comprasAmazon(pedido, p1, p2, p3, p4, p5))