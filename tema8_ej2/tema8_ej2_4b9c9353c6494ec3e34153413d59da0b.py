def buscarTodas(a,b):
    lista = []
    retorno = ""
    for i in range(len(a)):
        if a[i] == b:
            retorno = retorno + str(i) + " "
    return retorno[:-1]

if __name__ == "__main__":
    pass
           