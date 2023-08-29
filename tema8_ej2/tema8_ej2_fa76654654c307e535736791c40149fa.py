def buscarTodas(a,b):
    indices=[]
    for i in range(0,len(a)):
        if a[i]==b:
            indices.append(str(i))
    return " ".join(indices)