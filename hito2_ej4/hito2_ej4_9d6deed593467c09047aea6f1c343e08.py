carro = {}
precios = {1: 33.77,2: 203,3: 27.58,4: 348,5: 51.19}
descuentos = {frozenset((1, 2, 3)): 0.2,frozenset((4, 5)): 0.15}

while True:
    orden = input("Ingrese producto y cantidad (producto,cantidad), ver o checkout: ").split(",")
    if orden[0] == "checkout":
        total = sum(precios[int(p)]*c for p, c in carro.items())
        for productos, descuento in descuentos.items():
            if productos.issubset(carro.keys()):
                total *= 1 - descuento
        print("Total: $", round(total, 1))
        break

    elif orden[0] == "ver":
        print("Carro: ", "\n".join(str(cantidad) + "x Producto " + str(producto) + ", precio unitario: $" + str(precios[producto]) for producto, cantidad in carro.items()))

    else:
        producto, cantidad = int(orden[0]), int(orden[1])
        if producto in precios.keys():
            if producto in carro.keys():
                carro[producto] += cantidad
            else:
                carro[producto] = cantidad
            print("Producto", orden[0], "agregado con éxito.")
