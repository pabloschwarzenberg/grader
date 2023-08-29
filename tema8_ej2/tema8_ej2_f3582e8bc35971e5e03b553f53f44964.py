def buscarTodas(a,b):
    lista=[]
    i=0
    while i<len(a):
        if a[i]==b:
            lista.append(i)
        i=i+1
    cadena= " ".join(str(a) for a in lista)
    return cadena

if __name__ == "__main__":
    pass
           