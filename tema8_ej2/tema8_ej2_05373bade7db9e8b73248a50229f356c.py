def buscarTodas(a,b):
    lista=[]
    for i in range(len(a)):
        if a[i]==b:
            i=str(i)
            lista.append(i)
    numeros=" ".join(lista)
    return numeros
    

if __name__ == "__main__":
    pass
           