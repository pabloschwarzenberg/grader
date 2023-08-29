def buscarTodas(a,b):
    resul = []

    for i in range(len(a)):
        if (a[i] == b):
            resul.append(i)
            
    if (len(resul) == 0):
        return 'No existe'
    
    return (' '.join(map(str,resul )))

print(buscarTodas("tres tristes tigres" , "t"))           