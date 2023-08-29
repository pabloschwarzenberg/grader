def buscarTodas(texto,letra):
    largo=list(texto)
    palabra=""
    contador=0
    listita=[]
    final=len(texto)
    while contador<final:
        if texto[contador]==letra:
            palabra=palabra+str(contador)+" "
            listita.append(str(contador))
        contador=contador+1
    lista=list(palabra)
    lista.pop()
    cadena=" ".join(listita)
    return cadena