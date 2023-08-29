def buscarTodas(a,b):
    cont = 0
    ubicaciones = 0
    for i in a:
        if i == b:
            if ubicaciones != cont:
                ubicaciones = str(ubicaciones)+" "+str(cont)
        cont  = cont+1
    return ubicaciones