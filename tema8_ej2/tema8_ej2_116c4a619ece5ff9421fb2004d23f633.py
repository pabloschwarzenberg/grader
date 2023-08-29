def buscarTodas(a,b):
    cont = 0
    posiciones = 0
    for i in a:
        if i == b:
            if posiciones != cont:
                posiciones = str(posiciones)+" "+str(cont)
        cont  = cont+1
    return posiciones