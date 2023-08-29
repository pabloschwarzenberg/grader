def buscarTodas(a,b):
    L=[]
    n=0
    while n<len(a):
        if b.find(a[n])!=-1:
            c=str(a.find(b))
            L.append(c)
            a=list(a)
            a[int(c)]="_"
            a="".join(a)
            n+=1
        else:
            n+=1
    final=" ".join(L)
    return str(final)

if __name__ == "__main__":
    print(L)
    print(str(final))
           