def buscarTodas(a,b):
    c=[]
    i=0
    for letra in a:
        if letra==b:
            i=str(i)
            c+=i
            c+=" "
            i=int(i)
            i+=1
        else:
            i+=1
    c.pop()
    l="".join(c)
    return (l)

if __name__ == "__main__":
    a=input("Ingrese un texto: ")
    b=input("Ingrese lo que quiere buscar: ")
    print(buscarTodas(a, b))
