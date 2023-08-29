def buscarTodas(a,b):
    pass
    d=[]
    i=0
    n=0
    while i < len(a):
        j=a.find(b,n)
        if j==a.find(b,n-1):
            pass
        elif j==-1:
            pass
        else:
            d.append(j)
        n=n+1
        i=i+1
    d=str(d)
    d=d.replace(",","")
    d=d.replace("[","")
    d=d.replace("]","")
    return d
if __name__ == "__main__":
    a=str(input("ingrese un texto: "))
    b=str(input("Ingrese lo que quiere buscar en el texto (Se mostrata las posiciones donde estara): "))
    c=buscarTodas(a,b)
    print(c)