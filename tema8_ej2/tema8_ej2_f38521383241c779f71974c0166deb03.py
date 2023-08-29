def buscarTodas(a, b):
    lugar = ""
    numero = 0
    for i in a:
        if i == b:
            if lugar == "":
                numerostr = str(numero)
                lugar += numerostr
                numero += 1
            else:
                lugar += " "
                numerostr = str(numero)
                lugar += numerostr
                numero += 1
        else:
            numero += 1
    return lugar