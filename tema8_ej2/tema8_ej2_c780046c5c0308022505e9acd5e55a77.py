def buscarTodas(a,b):
    lista=list(a)
    index=''
    for c in range(0,len(a)):
        if lista[c]==b:
            if c!=len(a)-1:
                index=index+str(c)+' '
            else:
                index=index+str(c)
    index=index.rstrip(' ')
    return index

if __name__ == "__main__":
    pass
           