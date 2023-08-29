def buscarTodas(a,b):
    m=0
    n=1
    numeros=[]
    while m<=(len(a)-1):
        x=a.find(b,m,n)
        if x!=-1:
            numeros.append(str(x))
        m=m+1
        n=n+1
    y=" ".join(numeros)
    return y

if __name__ == "__main__":
    a=str(input("a: "))
    b=str(input("b: "))
    print(buscarTodas(a,b))
