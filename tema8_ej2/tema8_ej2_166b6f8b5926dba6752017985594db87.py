def buscarTodas(a,b):
    listaFrase=[]
    a=(a)
    b=(b)
    # frase=frase.replace(" ","")
    for indice in a:
        listaFrase.append(indice)
    listPosicionLetras=[]
    for posicion,caracter in enumerate(a):
        if(caracter== b):
            for indice in range (len(listaFrase)):
                if listaFrase[indice] == b :
                    listaFrase[posicion] = caracter
            listPosicionLetras.append(posicion)
    # listPosicionLetras=str(listPosicionLetras)[1:-1]
    listPosicionLetras=' '.join([str(elem) for elem in listPosicionLetras])
    # listPosicionLetras="".join(map(str,listPosicionLetras))
    return listPosicionLetras
    # print(*listPosicionLetras,sep=' ')
if __name__ == "__main__":
    b='t'
    a='tres tristes tigres'
    print(buscarTodas(a,b))