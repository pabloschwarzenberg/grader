def jerigonzo(string):
    lista = list(string)
    for i in range(len(lista)):
        if lista[i] == "a":
            lista[i] = "apa"
        if lista[i] == "e":
            lista[i] = "epe"
        if lista[i] == "i":
            lista[i] = "ipi"
        if lista[i] == "o":
            lista[i] = "opo"
        if lista[i] == "u":
            lista[i] = "upu"
    string = ""
    for i in lista:
        string = string + i
    return string