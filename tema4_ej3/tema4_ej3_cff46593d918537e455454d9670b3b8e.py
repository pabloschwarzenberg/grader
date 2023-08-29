def jerigonzo(string):
    lista_string = list(string)
    i=0
    while i< len(lista_string):
        if lista_string[i] == "a":
            lista_string.insert((i+1), "pa")
        elif lista_string[i] == "e":
            lista_string.insert((i+1), "pe")
        elif lista_string[i] == "i":
            lista_string.insert((i+1), "pi")
        elif lista_string[i] == "o":
            lista_string.insert((i+1), "po")
        elif lista_string[i] == "u":
            lista_string.insert((i+1), "pu")
        i=i+1



    string = "".join(lista_string)

    return string

if __name__ == "__main__":
    pass
         