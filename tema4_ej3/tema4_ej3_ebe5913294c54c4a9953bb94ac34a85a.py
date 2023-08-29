def jerigonzo(string):
    lista = list(string)
    for posicion in range(len(lista)):
        if lista[posicion] in "aeiou":
            lista[posicion] += "p" + lista[posicion]
    string = "".join(lista)
    return string
         