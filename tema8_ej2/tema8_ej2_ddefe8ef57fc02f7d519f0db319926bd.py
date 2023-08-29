def buscarTodas(a,b):
    cant = a.count(b)
    ind = 0
    indices = ""
    for i in range(cant):
        indic = a.find(b,ind,)
        indices = indices + str(indic) + " "
        ind = indic + 1
    return indices[:-1]

