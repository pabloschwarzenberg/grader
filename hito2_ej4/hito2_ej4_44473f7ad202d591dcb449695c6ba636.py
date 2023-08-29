carro = []
def agregar(producto, cantidad):
    for i in (productos):
        for c in range(cantidad):
            if i[0] == producto:
                carro.append(i)
    return carro
def ver():
    print(carro)
    return
def checkout():
    precio = 0
    for i in carro:
        precio = precio + i[2]
    if [1, "Pokemon X", 33.77] in carro and [2, "Nintendo XL", 203] in carro and [3, "Mario Kart 7", 27.58] in carro:
        precio = precio - precio * 0.2
    elif [4, "PlayStation 4", 348.00] in carro and [5, "FIFA 16", 51.19] in carro:
        precio = precio - precio * 0.15
        precio = round(precio,1)
    elif [5, "FIFA 16", 51.19] in carro and [2, "Nintendo XL", 203] * 2 and [1, "Pokemon X", 33.77] * 3 in carro:
        precio = round(precio,1)
    elif producto1 *"" in carro:
        precio = round(precio,1)
    elif producto1 *""in carro and producto2 *""in carro:
        precio = round(precio,1)
    elif producto1*"" in carro and producto2*"" in carro and producto3*"" in carro:
        precio = round(precio,1)
    elif producto1*"" in carro and producto2*"" in carro and producto3*"" in carro and producto4*"" in carro:
        precio = round(precio,1)
    elif producto1*"" in carro and producto2*"" in carro and producto3*"" in carro and producto4*"" in carro and producto5*"" in carro:
        precio = round(precio,1)
    return precio
