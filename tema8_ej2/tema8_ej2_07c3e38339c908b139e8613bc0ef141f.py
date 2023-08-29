def buscarTodas(a,b):
    busca=a.find(b)
    buscador=""+str(busca)+""
    contador = busca+1
    while contador<(len(a)):
        if a[contador]==b:
            buscador+=" "+str(contador)
            contador+=1

        else:
            contador+=1


    return buscador


           