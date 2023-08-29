def jerigonzo(string):
    vocales = ["a","e","i","o","u"]
    listapalabra = list(string)
    largo = len(string)
    r = 0
    for i in range(1,6):
        g = 0
        while g<largo:
            if listapalabra[g] == vocales[r]:
                listapalabra[g] = vocales[r]+"p"+vocales[r]
            g = g+1
        r = r+1
    string_2 = "".join(listapalabra)
    return string_2
         