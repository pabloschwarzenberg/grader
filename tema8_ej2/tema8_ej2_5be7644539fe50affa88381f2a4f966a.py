def buscarTodas(a,b):
    indice = ""
    for i in range(len(a)):
        if a[i] == b:
            indice = indice + str(i) + " "
        else:
            pass
    indices = indice[:-1]
    return indices
 
if __name__ == "__main__":
    pass
           