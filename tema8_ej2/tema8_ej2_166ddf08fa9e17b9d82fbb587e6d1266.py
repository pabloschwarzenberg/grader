def buscarTodas(a,b):
    letras = []
    for s in a:
        letras.append(s)
    indices = []
    indicesstr = ""
    
    temp = ""
    for i in range(len(letras)):
        if b in letras:
            if b == letras[i]:
                indices.append(letras.index(b))
                letras[i] = " "
    borrar = []
    for n in indices:
        n = str(n)
        indicesstr += n + " "
    indicesstr.rstrip()
    for i in indicesstr:
        borrar.append(i)
    borrar.pop()
   
    indicesstr = ""
    for e in borrar:
        indicesstr += e
    
    return indicesstr