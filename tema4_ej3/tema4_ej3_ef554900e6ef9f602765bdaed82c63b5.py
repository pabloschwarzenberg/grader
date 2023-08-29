def jerigonzo(string):
    vocales = ["a","e","i","o","u"]
    palabra = list(string)
    nueva_palabra = []
    for i in palabra:
        if i in vocales:
            nueva_palabra.append(i)
            nueva_palabra.append("p")
            nueva_palabra.append(i)
        else:
            nueva_palabra.append(i)
    nueva_palabra = "".join(nueva_palabra)
    return nueva_palabra

if __name__ == "__main__":
    pass