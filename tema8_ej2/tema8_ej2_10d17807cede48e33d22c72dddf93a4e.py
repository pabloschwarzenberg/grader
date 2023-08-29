def buscarTodas(a,b):
    palabra = []

    for i in range(len(a)):
        if (a[i] == b):
            palabra.append(i)
    if (len(palabra) == 0):
        return 'No existe'
    
    return (' '.join(map(str,palabra )))

print(buscarTodas('tres tristes tigres' , 't'))