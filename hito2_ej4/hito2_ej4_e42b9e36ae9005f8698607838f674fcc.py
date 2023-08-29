p1 = [1, "Pokemon X", 33.77]
p2 = [2, "Nintendo XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16", 51.19]
productos = [p1, p2, p3, p4, p5]
compra = []
listacompra = []
while True:
    command = input("")
    if ',' in command:
        commandData = command.split(",")
        producto = int(commandData[0])
        cantidad = int(commandData[1])
        listacompra.append(producto)
        compra.append([producto, cantidad])
    if command == "ver":
        for x in compra:
            i = productos[x[0] - 1]
            print(i[1] + ', USD ' + str(i[2]))
    if command == "checkout":
        usdtotal = 0
        descuento = 0
        if 1 in listacompra and 2 in listacompra and 3 in listacompra:
            descuento += 20
        if 4 in listacompra and 5 in listacompra:
            descuento += 15
        for x in compra:
            i = productos[x[0] - 1]
            usdtotal += i[2] * (100 - descuento) / 100
        usdtotal = round(usdtotal, 1)
        print(usdtotal)
