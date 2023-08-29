def buscarTodas(a,b):
    lista = []
    for i in range(len(a)):
        if(a[i]==b):
            lista.append(i)
    if(len(lista)==0):
        return "no existe"
    
    return lista
        

           