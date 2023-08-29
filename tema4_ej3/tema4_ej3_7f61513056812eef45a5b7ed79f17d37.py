def jerigonzo(string):
    lista = list(string)
    c=0
    while c < len(lista) :
        if lista[c] == "a":
            lista.insert((c+1) , "pa")
        elif lista[c] == "e":
            lista.insert((c+1) , "pe")
        elif lista[c] == "i":
            lista.insert((c+1) , "pi")
        elif lista[c] == "o":
            lista.insert((c+1) , "po")
        elif lista[c] == "u":
            lista.insert((c+1) , "pu")
        c = c + 1
    return "".join(lista)


if __name__ == "__main__":
    x = input("Ingrese la palabra que quiere cambiar a jerigonzo: ")
    y = jerigonzo(x)
    print(y)
    pass
