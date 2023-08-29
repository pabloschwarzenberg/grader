def buscarTodas(a,b):
    l=len(a)
    i=0
    e=""
    while i<=l:
        s=str(a[i:l])
        f = s.find(b)
        if f==0:
            k=str(i)
            e=e+k+" "
        i+=1
    e=e.strip()
    return e

if __name__ == "__main__":
    a=input("Ingrese una frase: ")
    b=input("Que letra quiere buscar en la frase? ")
    print(buscarTodas(a,b))
