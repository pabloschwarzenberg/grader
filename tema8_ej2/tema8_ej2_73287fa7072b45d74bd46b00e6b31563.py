lista = []
def buscarTodas (a,b) :
    for i in range (len(a)):
        if a[i] == b :
            lista.append(i)
            #print(lista)
    return lista
def imprimirLista(lista):
    print(str(lista[0])+" "+str(lista[1])+" "+str(lista[2])+" "+str(lista[3]))


a = "tres tristes tigres"
b = "t"
resultado = (buscarTodas(a,b))
imprimirLista(resultado)