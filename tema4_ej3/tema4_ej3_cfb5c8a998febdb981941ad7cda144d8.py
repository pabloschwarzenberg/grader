#Jerigonzo
def jerigonzo(string):
    palabra = list(string)
    for i in palabra:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            x = palabra.index(i)
            palabra[x] = i + "p" + i
    palabra1 = "".join(palabra)
    return palabra1