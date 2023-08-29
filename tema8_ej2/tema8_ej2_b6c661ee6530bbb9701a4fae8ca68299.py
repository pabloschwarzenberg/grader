def buscarTodas(a,b):
    posiciones = ""
    largo = len(a)
    for i in range(largo):
        if b == a[i]:
            posiciones += "{}".format(i)+" "
    posiciones = posiciones[:-1]
    return posiciones

if __name__ == "__main__":
    pass
           