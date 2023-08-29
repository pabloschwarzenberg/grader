def buscarTodas(a,b):
    cadena = ""
    i = 0
    while i < len(a):
        if a[i] == b:
            cadena = cadena + str(i) + " "
        i+=1
        if i == len(a):
            cadena = cadena[:-1]
    return cadena

