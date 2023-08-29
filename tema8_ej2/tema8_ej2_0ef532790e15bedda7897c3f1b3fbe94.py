def buscarTodas(a,b):
    contador=0
    palabra_acumulada=""
    for letra in a:
        if letra==b:
            palabra_acumulada=palabra_acumulada+str(contador)+" "
        contador=contador+1
    return palabra_acumulada[:-1]