def buscarTodas(x, y):
    lista = []
    for z in range(len(x)):
        if (y == x[z]):
            lista.append(z)
    a = lista[-1]
    b = str(lista)
    c = b.replace(",", "")
    c = c.replace("[","")
    c = c.replace("]","")
    return c
if "__name__" == "__main__":
    x = "tres tristes tigres"
    y = "t"
    print(buscarTodas(x, y))
           