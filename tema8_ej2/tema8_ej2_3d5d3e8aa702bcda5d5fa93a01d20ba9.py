def buscarTodas(a,b):
    a=list(a)
    d=[]
    for i in range(0,len(a)):
        if a[i]==b:
            d.append(str(i))
    d=list(d)
    d=" ".join(d)
    return d


    pass


if __name__ == "__main__":
    pass