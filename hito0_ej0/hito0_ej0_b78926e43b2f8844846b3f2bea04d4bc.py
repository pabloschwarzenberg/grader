items=[[1,3,4],[2,4,5],[3,7,10],[4,8,11],[5,9,13]]
def mochila(item,peso_max,carga,beneficio,cosas):
    conveniencia=0
    for i in item:
        if (i[2]/i[1]) > conveniencia:
            conveniencia=i[2]/i[1]
            item_selecto=i
    if carga+item_selecto[1]>peso_max:
        item.remove(item_selecto)
        if len(item)==0:
            return cosas
        return mochila(item,peso_max,carga,beneficio,cosas)
    peso_minimo=item[0][1]
    for i in item:
        if i[1]<peso_minimo:
            peso_minimo=i[1]
    if carga+peso_minimo>peso_max:
        return cosas
    cosas.append(item_selecto[0])
    carga+=item_selecto[1]
    beneficio+=item_selecto[2]
    return mochila(item,peso_max,carga,beneficio,cosas)
print(mochila(items,15,0,0,[]))