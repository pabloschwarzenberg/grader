def buscarTodas(a, b):
    indices = []
    longitud_b = len(b)
    
    for i in range(len(a)):
        if a[i:i+longitud_b] == b:
            indices.append(str(i))
    
    return ' '.join(indices)
 