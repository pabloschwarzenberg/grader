def buscarTodas(a,b):
    lista=list(a)
    listab=list(b)
    s=""
    cuenta=lista.count(b)
    for letra in lista:
        if letra==b:
            s=s+str((lista.index(letra)))+" "
            lista.insert((lista.index(letra)),"z")
            lista.remove(letra)
    s=s[:-1]
    return s

if __name__ == "__main__":
    a=input()
    b=input()
    print(buscarTodas(a,b))