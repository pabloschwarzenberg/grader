def buscarTodas(a,b):
    i = 0
    string = ""
    for caracter in a:
        if caracter == b:
            string +=" " + str(i)
        i += 1
    return(string.strip(" "))