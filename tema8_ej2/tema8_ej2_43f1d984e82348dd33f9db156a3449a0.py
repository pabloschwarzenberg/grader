def buscarTodas(a,b):
    q=[]
    k=a.count(b)
    l=list(a)
    while k>0:
        p=a.find(b)
        g="{} ".format(p)
        q.append(g)
        l[p]="_"
        a="".join(l)
        k-=1
    return ("".join(q)).strip()

if __name__ == "__main__":
    pass
           