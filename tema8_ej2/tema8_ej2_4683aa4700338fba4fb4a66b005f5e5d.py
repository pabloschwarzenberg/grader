def buscarTodas(a, b):

    indices = ''
    for i in range(len(a)):
        if a[i] == b:
            indices = indices + str(i) + ' '
        
    return indices[:-1]
           