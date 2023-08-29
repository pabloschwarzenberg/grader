def jerigonzo(string):
    string = list(string)
    lista = []
    for i in string:
        lista.extend(i)
        vocales = ["a", "e", "i", "o", "u"]
        if i in vocales:
            lista.extend("p")
            lista.extend(i)

    string = "".join(lista)

    return string
         