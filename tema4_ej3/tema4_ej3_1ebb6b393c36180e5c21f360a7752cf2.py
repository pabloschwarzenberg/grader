def jerigonzo(string):
    nuevo = ""
    vocales = ["a","e","i","o","u"]
    string.lower()
    for i in range(len(string)):
        if string[i] in vocales:
            nuevo += string[i] + "p" + string[i]
        else:
            nuevo += string[i]
    return nuevo
         