def buscarTodas(a,b):
    contador = 0
    string = ""
    for caracter in a:
        if caracter == b:
            string +=" " + str(contador)
        contador += 1
    return(string.strip(" "))         