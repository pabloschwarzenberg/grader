def buscarTodas(a,b):
    termino = []
    posicion = 0
    for i in a:
        if i == b:
            termino.append(posicion)
        posicion += 1
    string = ""
    for i in termino:
        string += str(i)+" "
    string = string[:-1]
    
    return(string)   
           