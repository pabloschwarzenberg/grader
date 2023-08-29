def jerigonzo(string):
    tolist = list(string)
    newstring = []
    vocales = ['a', 'e', 'i', 'o', 'u']
    for letra in tolist:
        newstring.append(letra)
        if letra in vocales:
            newstring.append("p" + letra)
    string = ''.join(newstring)
    return string



if __name__ == "__main__":
    pass
         