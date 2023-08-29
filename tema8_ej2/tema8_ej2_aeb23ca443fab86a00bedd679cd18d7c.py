def buscarTodas(a,b):
    index = []
    inicio = 0
    fin = len(a)
    lista = list(a)
    while True:
        try:
            pos = lista.index(b, inicio, fin)
            index.append(str(pos))
            inicio = pos + 1
        except ValueError:
            break

    return index
    
if __name__== "__main__":
    a=input("Ingrese la palabra:")
    b=input("Ingrese la letra a buscar:")
    cuenta = buscarTodas(a,b)
    print (" " .join(cuenta))