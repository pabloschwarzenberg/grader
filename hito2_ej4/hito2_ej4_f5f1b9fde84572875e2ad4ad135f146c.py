p1 = [1, "Pokemon X", 33.77]
p2 = [2, "Nintendo XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16", 51.19]

carro = []

ordenes = [
    "3,1",  # Agregar 1 unidad del producto 3
    "5,2",  # Agregar 2 unidades del producto 5
    "2,3",  # Agregar 3 unidades del producto 2
    "checkout"  # Realizar el checkout
]

for orden in ordenes:
    if orden == "ver":
        if len(carro) == 0:
            print("El carro está vacío.")
        else:
            print("Productos en el carro:")
            for producto in carro:
                print(producto[1], "x", producto[3])

    elif orden == "checkout":
        total = 0

        if len(carro) == 0:
            print("El carro está vacío.")
        else:
            for producto in carro:
                total += producto[2] * producto[3]

            # Aplicar descuento si se cumplen las condiciones
            if any(producto[0] in [1, 2, 3] for producto in carro) and \
                    any(producto[0] in [4, 5] for producto in carro):
                total *= 0.8  # Aplicar descuento del 20%
            elif all(producto[0] in [4, 5] for producto in carro):
                total *= 0.85  # Aplicar descuento del 15%

            print("Total a pagar: $", round(total, 1))

    else:
        try:
            producto, cantidad = map(int, orden.split(","))
            if producto in [1, 2, 3, 4, 5] and cantidad > 0:
                if producto == 1:
                    producto_info = p1
                elif producto == 2:
                    producto_info = p2
                elif producto == 3:
                    producto_info = p3
                elif producto == 4:
                    producto_info = p4
                elif producto == 5:
                    producto_info = p5

                carro.append([producto, producto_info[1], producto_info[2], cantidad])
                print("Se agregó", producto_info[1], "x", cantidad, "al carro.")
            else:
                print("Orden inválida.")
        except ValueError:
            print("Orden inválida.")


