def buscarTodas(a,b):
    pass
    lista=list(a)
    m=[i for i, x in enumerate(lista) if x==b]
    lista2=list(m)
    string=" ".join(str(x) for x in lista2)
    return string

if __name__ == "__main__":
    pass
    a=input("ingrese a ")
    b=input("ingrese b ")
    print(buscarTodas(a,b))
