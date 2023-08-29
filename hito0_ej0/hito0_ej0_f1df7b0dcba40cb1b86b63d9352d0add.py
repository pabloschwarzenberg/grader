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
    #primero revisamos el peso, si se pasa del peso no seguimos explorando
    if peso>capacidad:
        return
    valor=beneficio(mochila)
    mejor_valor=beneficio(mejor_mochila)
    #si es mayor el beneficio cambiamos la mejor solución
    if valor > mejor_valor:
        #el clear importa para que podamos pasar una lista
        #como parámetro en el que queremos que quede el mejor
        #resultado, la otra forma es retornar el valor
        mejor_mochila.clear()
        for item in mochila:
            mejor_mochila.append(item)
        print(valor)

    #tengamos o no una mejor solución, seguimos tratando de agregar items
    #en la mochila.
    for item in items:
        mochila.append(item)
        resolver(mochila,items,capacidad,mejor_mochila)
        mochila.pop()

    #esto es una forma de retornar el último valor de un parámetro
    #en el que construimos la solución, al final de todas las llamadas
    #recursivas
    #cuando terminan todas las llamadas recursivas, quedamos en la primera
    #llamada a la función resolver, en donde la mochila llegó como un
    #parámetro vacío, así sabemos cuando podemos retornar un valor
    if mochila==[]:
        return mejor_mochila

     