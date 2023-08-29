def buscarTodas(a,b):
    listado = []
    info = ""
    for i in range(len(a)):
        if(a[i]==b):
            listado.append(i)
            c = [str(x) for x in listado]
    info = " " .join(c)
    
    return info