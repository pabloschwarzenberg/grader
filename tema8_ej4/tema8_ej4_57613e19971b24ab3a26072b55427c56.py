def rot13(palabra):
    lista = list(palabra)
    alphabet1 = list("abcdefghijklm")
    alphabet2 = list("nopqrstuvwxyz")
    for i in range(len(lista)):
        for j in range(len(alphabet1)):
            if lista[i] == alphabet1[j]:
                lista[i] = alphabet2[j]
            elif lista[i] == alphabet2[j]:
                lista[i] = alphabet1[j]
    new_list = "".join(lista)
    return new_list