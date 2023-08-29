def buscarTodas(a,b):
    indice=0
    lista=[]
    flag= True
    while indice<len(a) and flag:
        if a[indice:].find(b)==-1:
            flag=False
        else:
            c=a[indice:].find(b)
            indice=indice+1+c
            lista.append(str(indice - 1))
    return " ".join(lista)

if __name__ == "__main__":
    pass
           