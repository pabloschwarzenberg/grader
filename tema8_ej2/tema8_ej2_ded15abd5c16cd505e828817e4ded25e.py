def buscarTodas(a,b):
    c=[]
    d=0
    while True:
        if (a.find(b))!=-1:
            a2=list(a)
            c.append(str(a.find(b)+d))
            a2.remove(b)
            a="".join(a2)
            d+=1
        else:
            c2=" ".join(c)
            return c2
    pass

if __name__ == "__main__":
    pass
           