def buscarTodas(a,b):
    listA = list(a)
    string = []
    for letra in list(a):
        if letra == b:
            string.append(str(listA.index(letra)))
            listA[listA.index(letra)] = ''
    indices = " ".join(string)
    return indices 

if __name__ == "__main__":
    pass
           