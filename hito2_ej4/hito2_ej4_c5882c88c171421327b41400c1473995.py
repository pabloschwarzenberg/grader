p1 = [1, "Pokemon X", 33.77]
p2 = [2, "Nintendo XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16", 51.19]
option = ""

def ver():
    print([1, "Pokemon X", 33.77])
    print([2, "Nintendo XL", 203])
    print([3, "Mario Kart 7", 27.58])
    print([4, "PlayStation 4", 348.00])
    print([5, "FIFA 16", 51.19])

def checkout():
    pass

carro = []
while True:
    option = input("Seleccione su opción ver o checkout: ")
    if option == "ver":
        ver()
    elif option == "checkout":
        si = True
        while si:
            si = input("Agregue un producto")
            if si == "si":
                product = input("Numero producto")
                cant = input("Cantidad a comprar")
                buy = str(product) + "," + str(cant)
                carro.append(buy)
            carro.append("checkout")
        checkout(carro)

    else:
        print("Opcion no valida")