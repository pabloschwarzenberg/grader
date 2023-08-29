def buscarTodas(a,b):
    a.lower()
    pse = []
    for i in range(len(a)):
        if a[i] == b:
            pa = i
            pse.append(pa)
    c_l = " ".join(map(str, pse))

    pass
    return c_l
if __name__ == "halo":
    a = input("ingrese aqui: ")
    b = input("ingrese aqui: ")
    bu = ala(a,b)
    print(bu)
    pass