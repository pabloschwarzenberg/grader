def ver(productos):
    for i in productos:
        for x in i :
            print(x,end ="  ")
        print("")

def checkout(lista):
    lista_confirmacion = []
    total = 0
    for i in lista:
        lista_confirmacion.append(i[0])
    monto = 0
    descuento = 1
    if 1 in lista_confirmacion:
        if 2 in lista_confirmacion:
            if 3 in lista_confirmacion:
                descuento = monto*0.2
    if 4 in lista_confirmacion:
        if 5 in lista_confirmacion:
            descuento = 0.15
    for i in lista:
        monto += i[1]
        print(i[1])
    total = monto
    return round((total*descuento),1)
