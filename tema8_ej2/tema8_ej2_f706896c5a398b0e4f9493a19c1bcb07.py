def buscarTodas(a,b):
    a=list(a)
    indices=[]
    for i in range(len(a)):
        if a[i]==b:
            indices.append(str(i))
    indices=' '.join(indices)
    return indices

if __name__ == "__main__":
    pass
           