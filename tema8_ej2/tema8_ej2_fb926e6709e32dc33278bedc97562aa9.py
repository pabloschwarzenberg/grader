def buscarTodas(a,b):
    c = []
    i=0
    while True:
        n=a[i:].find(b)
        
        if n==-1:
            break
        else:
            c.append(str(n+i))
            i+=n+1
    c = " ".join(c)
    return c

if __name__ == "__main__":
    pass
           