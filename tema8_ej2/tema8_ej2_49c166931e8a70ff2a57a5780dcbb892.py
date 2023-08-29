def buscarTodas(a,b):
    i=0
    l=[]
    while i<len(a):
        if a[(i)]==b:
            l.append(i)
        i=i+1
    j=0
    while j<len(l):
        l[j]=str(l[j])
        j=j+1
    l=" ".join(l)
    return l


if __name__ == "__main__":
    pass
           