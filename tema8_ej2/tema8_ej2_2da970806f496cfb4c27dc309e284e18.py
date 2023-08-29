def buscarTodas(a,b):
    x=[]
    a=list(a)
    i=0
    while i<len(a):
        if b==a[i]:
            x.append(i)
        i=i+1
    x=" ".join(str(t) for t in x)
    return x
if __name__ == "__main__":
    a=input("ingrese un string:")
    b=input("ingrese lo que desea buscar dentro del string:")
    print(buscarTodas(a,b))