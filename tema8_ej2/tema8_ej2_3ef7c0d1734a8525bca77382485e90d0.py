def buscarTodas(a,b):
    lista_a=list(a)
    indices=[]
    for index, letter in enumerate(lista_a):
        if letter==b:
            index1=str(index)
            indices.append(index1)
    string=" ".join(indices)
    return string
    
    pass

if __name__ == "__main__":
    pass
          