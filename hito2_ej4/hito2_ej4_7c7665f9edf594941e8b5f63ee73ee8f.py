productos = [
    ['1', "Pokemon X", 33.77],
    ['2', "Nintendo XL", 203],
    ['3', "Mario Kart 7", 27.58],
    ['4', "PlayStation 4", 348.00],
    ['5', "FIFA 16", 51.19]]
carro = []
llamada = False

def agregar(producto, cantidad):
    for i in (productos):
        if i[0] == producto:
            for n in range(int(cantidad)):
                carro.append(i)

    return carro

def ver():
    print(carro)
    return

def checkout():
    global llamada
    llamada = True
    precio = 0
    for i in carro:
        precio = precio + i[2]
    if [1, "Pokemon X", 33.77] in carro and [2, "Nintendo XL", 203] in carro and [3, "Mario Kart 7", 27.58] in carro:
        precio = precio - precio * 0.2
    elif [4, "PlayStation 4", 348.00] in carro and [5, "FIFA 16", 51.19] in carro:
        precio = precio - precio * 0.15
    precio = round(precio,1)
    return precio


while llamada == False:
    funcion = str(input("Ingresar valores de función: "))
    try:
        agregar(funcion[0],funcion[2])
    except:
        pass
    if funcion == 'checkout':
        print(checkout())
    elif funcion == 'ver':
        ver()