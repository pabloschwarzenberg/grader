def buscarTodas(a,b):
    lista=list(a)
    nueva=[]
    j=0
    for i in lista:
        if i==b:
            nueva.append(str(j))
        j=j+1
    
    numeros=" ".join(nueva)
    return numeros
    pass

if __name__ == "__main__":
    pass
           