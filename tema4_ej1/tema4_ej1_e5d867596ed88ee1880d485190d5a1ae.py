import random
def ocultar_letras(termino,dosis):
    reciente = list(termino)
    for i in range(0, dosis):
        variacion = False
        while variacion == False:
            n=random.randint(0,len(termino)-1)
            if reciente[n] != '_':
                reciente[n] = '_'
                variacion = True
    return ''.join(reciente)
def revisar_letra(termino_secreto,termino,letras):
    reciente=list(termino)
    for i in range(0,len(termino)):
        if termino[i] == '_':
            if termino_secreto[i]==letras:
                reciente[i]= letras
    return ''.join(reciente)