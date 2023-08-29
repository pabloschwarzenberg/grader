def jerigonzo(string):
    lista = []
    for i in range(len(string)):
        if (string[i] == "a") or (string[i] == "e") or (string[i] == "i") or (string[i] == "o") or (string[i] == "u"):
            lista.append(string[i])
            lista.append("p")
            lista.append(string[i])
        else:
            lista.append(string[i])
    string2 = "".join(lista)
    return string2