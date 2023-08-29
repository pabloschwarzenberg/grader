def buscarTodas(a,b):
    lisFrase=[]
    for i in range(len(a)):
        lisFrase.append(a[i])
    

    lisIndices=[]

    for i in range(0,len(lisFrase)):
        if lisFrase[i]==b:
            lisIndices.append(str(i)+ " ")
    indices="".join(lisIndices)
    indicesSinEspacio=indices.rstrip()
    return(indicesSinEspacio)

           