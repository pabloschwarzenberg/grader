def buscarTodas(a, b):
    li = []
    for i in range(len(a)):
        if (b == a[i]):
            li.append(i)
    x = li[-1]
    y = str(li)
    z = y.replace(",", "")
    z = z.replace("[","")
    z = z.replace("]","")
    return z
