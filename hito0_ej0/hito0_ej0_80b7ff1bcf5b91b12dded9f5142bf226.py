#Problema mochila

#peso max 17

#Item     Peso    Beneficio
#1        3       4
#2        4       5
#3        7       10
#4        8       11
#5        9       13

#articulos=[[item, peso,beneficio]]

def peso(articulos,opciones):
    peso_mochila=0
    for articulo in opciones:
        if articulo[0] in articulos:
            peso_mochila=peso_mochila+articulo[1]
    return peso_mochila

def beneficio(articulos,opciones):
    ben=0
    for articulo in articulos:
        for i in opciones:
            if i[0]==articulo:
                ben=ben+i[2]
    return ben

def mochila(Peso,articulos,opciones,maximo=[]):
    peso_mochila=peso(articulos,opciones)
    benef=beneficio(articulos,opciones)
    if peso_mochila>0 and peso_mochila<=Peso:
        print(articulos)
    elif peso_mochila>Peso:
        return
    for a in opciones:
        if a[0] not in articulos:
            articulos.append(a[0])
            mochila(Peso,articulos,opciones,maximo)
            articulos.pop()

items=[[1,3,4],[2,4,5],[3,7,10],[4,8,11],[5,9,13]]
mochila(17,[],items)