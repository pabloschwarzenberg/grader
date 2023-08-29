def buscarTodas(a,b):
    i = ""
    numero = 0
    for x in a:
        numero_str = str(numero)
        if x == b:
            if i == "":
                i += numero_str
            else:
                i += " "
                i += numero_str
        numero += 1
    return i

if "name" == "main":
    pass
           