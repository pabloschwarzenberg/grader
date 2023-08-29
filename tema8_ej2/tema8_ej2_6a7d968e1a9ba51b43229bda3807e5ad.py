def buscarTodas(a,b):
    c = ""
    for cont in range(0, len(a)-1):
        if(len(c) == 0):
            if(a[cont] == b):
                c = c + str(cont)
        elif(a[cont] == b):
            c = c + " "
            c = c + str(cont)
    return c
