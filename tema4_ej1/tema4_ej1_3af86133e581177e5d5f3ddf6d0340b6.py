def funcion_1(letra,lista):
    if len(lista)>0:
        for idx in range(len(lista)):
            if letra==lista[idx]:
                return 1
        lista.append(letra)
    else:
        lista.append(letra)
    return 0
def funcion_2(letra,word,lista):
    pos=0
    indicador=0
    for l in word:
        if letra==l:
            pos=word.index(l,pos)
            lista[pos]=letra
            pos=pos+1
            indicador=1
    if indicador==0:
        return True
    return lista
