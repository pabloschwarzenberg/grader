def jerigonzo(string):
    lista_nueva = []
    for x in string:
        if 'a' == x or 'e' == x or 'i' == x or 'o' == x:
            lista_nueva.append(x)
            lista_nueva.append('p')
            lista_nueva.append(x)
        else:
            lista_nueva.append(x)
        string = "".join(lista_nueva)
    return string

if __name__ == "__main__":
    pass
         