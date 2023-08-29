
def jerigonzo(string):
    vocales = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    i = 0
    contador = 0
    string = list(string)
    while i < len(string):
        for j in vocales:
            if string[i] == j:
                string[i] = string[i] + "p" + string[i]
        i += 1
    string= "".join(string)
    return string