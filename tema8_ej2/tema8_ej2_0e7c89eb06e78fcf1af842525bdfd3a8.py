def buscarTodas(a,b):
    lista = []
    i = 0
    for x in range(len(a)):
        if a[x] == b:
            lista.append(str(x))
        i = i + 1
     
    return " ".join(lista)
if __name__ == "__main__":
    print(buscarTodas("hola mundo", "o"))