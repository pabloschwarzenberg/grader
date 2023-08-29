def buscarTodas(a,b):
    lista= []
    cadena = ""

    for i in range(len(a)):

        if (a[i]==b):
            lista.append(i)
            c = [str(x) for x in lista]
    cadena = ' '.join(c)
    return cadena
           