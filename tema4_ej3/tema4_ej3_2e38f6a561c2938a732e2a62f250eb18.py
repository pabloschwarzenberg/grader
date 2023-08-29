def jerigonzo(string):
    string = list(string)
    lista = []
    for i in string:
        if i in "aeiou":
            lista.append("{}p{}".format(i, i))
        else:
            lista.append(i)
    return "".join(lista)
