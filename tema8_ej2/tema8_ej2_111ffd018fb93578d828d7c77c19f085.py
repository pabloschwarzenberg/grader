def buscarTodas(a, b):
    lista = []
    for g in range(len(a)):
        if (b == a[g]):
            lista.append(g)
    x = lista[-1]
    y = str(lista)
    z = y.replace(",", "")
    z = z.replace("[","")
    z = z.replace("]","")
    return z
if __name__ == "__main__":
    a = "tres tristes tigres"
    b = "t"
    print(buscarTodas(a, b))