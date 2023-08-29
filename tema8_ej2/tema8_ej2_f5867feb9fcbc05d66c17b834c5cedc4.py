def buscarTodas(a,b):
    posiciones = ""
    numero = 0
    for i in a:
        if i == b:
            if posiciones == "":
                numerostr = str(numero)
                posiciones += numerostr
                numero += 1
            else:
                posiciones += " "
                numerostr = str(numero)
                posiciones += numerostr
                numero += 1
        else:
            numero += 1
    return posiciones