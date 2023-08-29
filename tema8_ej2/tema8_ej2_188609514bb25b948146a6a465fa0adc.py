def buscarTodas(a, b):
    j = []
    k = 0
    for i in a :
        if i == b :
            j.append(str(k) + " ")
        k += 1
    j = "".join(j)
    j = j[ :-1]
    return j  