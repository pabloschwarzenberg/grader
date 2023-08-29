def buscarTodas(a,b):
    l = []
    inicio = 0
    while True:
        i = a.find(b, inicio)
        if i == -1: break
        l.append(i)
        inicio = i + 1
    return  " ".join(str(x) for x in l)

if __name__ == "__main__":
    a=str(input("Ingrese una palabra: "))
    b=str(input("Ingrese la palabra a buscar: "))
    print(buscarTodas(a,b))
           