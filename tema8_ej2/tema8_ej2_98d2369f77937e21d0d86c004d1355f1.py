def buscarTodas(a, b):
    c = 0
    vacio = ""
    for i in a:
        if i == b:
            if vacio == "":
                l = str(c)
                vacio += l
                c += 1
            else:
                vacio += " "
                l = str(c)
                vacio += l
                c += 1
        else:
            c += 1
    return vacio


if __name__ == "main_":
    print("Al buscar t en'tres tristes tigres' el resultado debiera ser", buscarTodas("tres tristes tigres", "t"))