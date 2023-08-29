def buscarTodas(a,b):
    g=[]
    for i in range(0,len(a)):
        count= 0
        for j in range(0,len(b)):
            if a[i+j]== b[j]:
                count=count+1
            if count== len(b):
                g.append(" "+str(i))
    g= "".join(g)

    return g[1:]

if __name__ == "__main__":
    pass
           