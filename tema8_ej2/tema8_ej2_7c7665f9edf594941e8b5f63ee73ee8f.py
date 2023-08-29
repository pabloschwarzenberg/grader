def buscarTodas(a,b):
    stringreturn = ''
    contador = 0
    while contador < len(a):
        if a[contador] == b:
            stringreturn = stringreturn + str(contador) + ' '
        contador = contador + 1
    cifras = stringreturn[:-1] 
    return cifras