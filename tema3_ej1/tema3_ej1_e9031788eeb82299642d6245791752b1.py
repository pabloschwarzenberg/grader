def suma_divisores(y):
    lista = []
    a = 0
    for z in range(1,y):
        if y % z == 0:
            a = a + z
            lista.append(z)
    if len(lista)==1:
        z = True
    else:
        z = False
    return a, z