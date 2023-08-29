def buscarTodas(a,b):
    lista = [a]
    for i in range(len(a)):
        if(a[i]==b):
            lista.append(i)
    if(len(lista)==0):
        return "no existe"
    
    return lista

        
print(buscarTodas("tres tristes tigres","t"))  
           