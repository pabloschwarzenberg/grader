def jerigonzo(string):
    lista = []
    vocales = ['a','e','i','o','u']
    for letra in string:
        lista.append(letra)
        for vocal in vocales:
            if vocal == letra:
                lista.append('p')
                lista.append(vocal)
    string = ''
    for x in lista:
        string += x
    return string
if __name__ == "__main__":
    pass
         