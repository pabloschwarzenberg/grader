def buscarTodas(a, b):
    lista = []
    for i in range(len(a)):
        if (b == a[i]):
            lista.append(i)
    x = lista[-1]
    y = str(lista)
    w = y.replace(",", "")
    w = w.replace("[","")
    w = w.replace("]","")
    return w
if __name__ == "__main__":
    a = "tres tristes tigres"
    b = "t"
    print(buscarTodas(a, b))