items=[[1,3,4],[2,4,5],[3,7,10],[4,8,11],[5,9,13]]

def evaluar(mochila):
    peso=0
    for item in mochila:
        peso=peso+item[1]
    return peso

def beneficio(mochila):
    valor=0
    for item in mochila:
        valor=valor+item[2]
    return valor

def resolver(mochila,items,capacidad,mejor_mochila):
    peso=evaluar(mochila)
    if peso>capacidad:
        return
    valor=beneficio(mochila)
    mejor_valor=beneficio(mejor_mochila)
    if valor > mejor_valor:
        mejor_mochila.clear()
        for item in mochila:
            mejor_mochila.append(item)
        print(valor)
    for item in items:
        mochila.append(item)
        resolver(mochila,items,capacidad,mejor_mochila)
        mochila.pop()

    if mochila==[]:
        return mejor_mochila

solucion=resolver([],items,17,[])
print(solucion)      