def buscarTodas(a,b):
    lista=[]
    for x in range(len(a)):
        if a[x]==b:
            lista.append(x," ")
    stra = " ".join(str(e) for e in lista)        
    return stra
if __name__ == "__main__":
    pass
           