def jerigonzo(string):
    vocales = ["a","e","i","o","u"]
    lista = string.split()
    texto =""
    pos_i = 0
    for i in lista:
        if pos_i != 0:
            texto+=" "
            for j in i:
                if j in vocales:
                    texto+=j+"p"+j
                else:
                    texto+=j

        else:
            for j in i:
                if j in vocales:
                    texto+=j+"p"+j
                else:
                    texto+=j
        pos_i += 1
    return texto