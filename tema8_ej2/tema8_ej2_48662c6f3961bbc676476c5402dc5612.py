def buscarTodas(a,b):
    coincidencias = []
    for i in range(len(a)):
        if a[i] == b:
            coincidencias.append(str(i))

    string = ' '.join(coincidencias)
    return string
