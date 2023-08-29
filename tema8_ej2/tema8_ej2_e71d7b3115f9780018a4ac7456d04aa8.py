def buscarTodas(a,b):
    posiciones = "0"
    numero = 1
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

if __name__ == "__main__":
    palabra1 = "tres tristes tigres"
    palabra1 = buscarTodas(palabra1,"t")
    print(palabra1)
    pass
           