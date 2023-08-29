def ver() :
    p1=[1,"Pokemon X",33.77]
    p2=[2,"Nintendo XL",203]
    p3=[3,"Mario Kart 7",27.58]
    p4=[4,"PlayStation 4",348.00]
    p5=[5,"FIFA 16",51.19]
    listproduc = []
    listproduc.append(p1)
    listproduc.append(p2)
    listproduc.append(p3)
    listproduc.append(p4)
    listproduc.append(p5)
    return listproduc

producto = "n"
precio = 0
listcompra = []
totales = []
descuento = 0
while producto != "checkout" :
    suma = 0
    listcont = 1
    producto = input("Ingrese su producto y cantidad : ")
    if producto != "checkout":
        listcompra.append(producto[0])
        array = ver()
        if producto == "ver":
            for proc in array :
                print(proc)
        else:
            for col in array :
                if col[0] == float(producto[0]) :
                    precio = col[2]
            total = precio * float(producto[2])
            totales.append(total)
            for result in totales :
                suma = suma + float(result)
            descuento = suma
            if '1' in listcompra :
                if '2' in listcompra :
                    if '3' in listcompra :
                        descuento = suma - (suma * 20 / 100)
            if '4' in listcompra :
                if '5' in listcompra :
                    descuento = suma - (suma * 15 / 100)
print(round(descuento,1))
    