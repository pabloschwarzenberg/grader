def buscarTodas(a,b):
    i=0
    x=""
    while i<len(a):
        if b in a[i:i+len(b)]:
            x=str(x)+str(i)+" "
        i+=1
    return str(x)
if __name__ == "__main__":
    buscarTodas(a,b)
           