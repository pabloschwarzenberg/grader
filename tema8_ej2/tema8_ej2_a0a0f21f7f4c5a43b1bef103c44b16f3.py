def buscarTodas(a,b):
    palabra = ""
    cont = 0
    for i in a:
        if i == b:
            palabra += str(cont)
            palabra += " "
        cont+=1
    return palabra.strip(" ")
