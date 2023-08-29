def buscarTodas(a,b):
    lista = []
    for i, c in enumerate(a):
            if b == c:
                lista.append(str(i))
    x = " ".join(lista)
    return x

if __name__ == "__main__":
    pass
           