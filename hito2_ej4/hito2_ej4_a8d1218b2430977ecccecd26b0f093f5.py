productos = [
    [1, "Pokemon X", 33.77],
    [2, "Nintendo XL", 203],
    [3, "Mario Kart 7", 27.58],
    [4, "PlayStation 4", 348.00],
    [5, "FIFA 16", 51.19]
]
listadcto = []
listacompras = []
monto_123 = 0
monto_45 = 0
print(f"1. Comprar\n2. Ver compra\n3. Checkout\n4. Salir")
opcion = 0
while opcion != 4:
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        for producto in productos:
            print(producto[0], "-", producto[1], "- $", producto[2])
        compra = input("Ingrese producto a comprar y cantidad (producto,cantidad): ")
        v = compra.split(",")
        producto = int(v[0])
        cantidad = int(v[1])
        if producto == 1:
            nombreprod = "Pokemon X"
            costoprod = 33.77
            monto_123 = monto_123 + (costoprod * cantidad)
            listadcto.append(1)
            for i in range(cantidad):
                listacompras.append(nombreprod) 
        elif producto == 2:
            nombreprod = "Nintendo XL"
            costoprod = 203
            monto_123 = monto_123 + (costoprod * cantidad)
            listadcto.append(2)
            for i in range(cantidad):
                listacompras.append(nombreprod)
        elif producto == 3:
            nombreprod = "Mario Kart 7"
            costoprod = 27.58
            montmonto_123o = monto_123 + (costoprod * cantidad)
            listadcto.append(3)
            for i in range(cantidad):
                listacompras.append(nombreprod)
        elif producto == 4:
            nombreprod = "PlayStation 4"
            costoprod = 348
            monto_45 = monto_45 + (costoprod * cantidad)
            listadcto.append(4)
            for i in range(cantidad):
                listacompras.append(nombreprod)
        elif producto == 5:
            nombreprod = "Fifa 16"
            costoprod = 51.19
            monto_45 = monto_45 + (costoprod * cantidad)
            listadcto.append(5)
            for i in range(cantidad):
                listacompras.append(nombreprod)
    elif opcion == 2:
        print("Productos seleccionados:")
        for produc in listacompras:
            print(produc)
        print(f"Monto productos: ${round(monto_45+monto_123,1)}, los descuentos se pondrán en el checkout.")
    elif opcion == 3:
        if 1 and 2 and 3 in listadcto:
            monto_123 = (monto_123 * 80) / 100
        if 4 and 5 in listadcto:
            monto_45 = (monto_45 * 85) / 100
        print(f"Total a pagar: ${monto_45+monto_123}")
