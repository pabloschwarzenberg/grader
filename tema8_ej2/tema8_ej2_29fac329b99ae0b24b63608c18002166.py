def buscarTodas(string, letra):
    string = str(string)
    letra = str(letra)
    lista_pos = ""
    for i in range(len(string)):
        if i == 0:
            if string[i] == letra:
                lista_pos = str(i)
        else:
            if string[i] == letra:
                lista_pos += " " + str(i)
    return lista_pos