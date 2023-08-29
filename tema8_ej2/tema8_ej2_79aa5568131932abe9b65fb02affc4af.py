def buscarTodas(a,b):
    i=0
    contador=[]
    a1=list(a)
    while i<len(a1):
        if a1[i]==b:
            contador.append(str(i))
        i=i+1

    f2=" ".join(contador)
    return f2

    

if __name__ == "__main__":
    pass
           