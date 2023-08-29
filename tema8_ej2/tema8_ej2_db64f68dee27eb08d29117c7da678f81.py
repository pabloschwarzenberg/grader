def buscarTodas(a,b):
    u=0
    lista=[]
    while a.find(b,u)!=-1:
        n=a.find(b,u)
        lista.append(n)
        u=n+1
    r=""
    for i in lista:
        r=r+str(i)+" "
    r=r[:-1]    
    return r
if __name__ == "__main__":
    a=input("Ingrese el string en el que quiere buscar: ")
    b=input("Ingrese el string que quiere encontrar: ")
    n=buscarTodas(a,b)
    print(n)

           