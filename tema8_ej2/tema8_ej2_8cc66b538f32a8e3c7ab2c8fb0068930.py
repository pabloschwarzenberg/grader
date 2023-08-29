def buscarTodas(a,b):
    x=True
    n=0
    lista=[]
    a1=a
    while x==True:
        if b in a:
            n=a.find(b) + len(a1)-len(a)
            lista.append(str(n))
            a=a[(a.find(b)+1):]
        else:
            x=False
    resultado=" ".join(lista)
    return resultado

if __name__ == "__main__":
    a=input("String 1: ")
    b=input("String 2: ")
    print(buscarTodas(a,b))