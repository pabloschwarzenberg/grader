def jerigonzo(string):
    vocales = ["a", "e", "i", "o", "u"]
    cosa = []
    for i in range(len(string)):
        cosa.append(string[i])
    for i in range(len(cosa)):
        if cosa[i] in vocales:
            cosa[i] = cosa[i] + "p" + cosa[i]
    string = "".join(cosa)
    return string
