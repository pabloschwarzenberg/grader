def buscarTodas(a,b):
    a.lower()
    ps = []
    for i in range(len(a)):
        if a[i] == b:
            p = i
            ps.append(p)
    c_l = " ".join(map(str, ps))

    pass
    return c_l
    a = input("ingrese aqui: ")
    b = input("ingrese aqui: ")
    bu = al(a,b)
    print(bu)
    pass