def buscarTodas(a,b):
    i = ""
    Numero = 0
    for x in a:
        Numero_str = str(Numero)
        if x == b:
            if i == "":
                i += Numero_str
            else:
                i += " "
                i += Numero_str
        Numero += 1
    return i