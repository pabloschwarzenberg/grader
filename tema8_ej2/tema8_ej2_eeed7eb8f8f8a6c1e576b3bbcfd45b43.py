def buscarTodas(a, b):

    var_Numero = 0
    var_PosicionIndice = str()

    for indice in a:
        if indice == b:
            if var_PosicionIndice == "":
                var_PosicionIndice += str(var_Numero)
                var_Numero += 1
            else:
                var_PosicionIndice += (" " + str(var_Numero))
                var_Numero += 1
        else:
            var_Numero += 1
    
    return var_PosicionIndice

if __name__ == "__main__":
    pass