def jerigonzo(t):
    vocales = ["a","i","u","e","o","A","I","U","E","O"]
    t_lista = list(t)
    for i in t_lista:
        if i in vocales:
            t_lista.insert(t_lista.index(i)+1,"p"+i)
        t = "".join(t_lista)
    print(t)

    return t