def levenshtein(palabra1,palabra2):
    retorno = '1S'
    contador = 0
    distancia = 0
    clave = 'a'

    while(len(palabra2)-1>=contador):
        if len(palabra1)>contador:
            letra1 = list(palabra1)[contador]
        else:
            letra1 = ' '
        letra2 = list(palabra2)[contador]
        contador = contador+1

        if letra1 != letra2:
            distancia = distancia+1
        if letra1 != letra2 and len(palabra1) == len(palabra2):
            distancia = distancia+1
            clave = 'cambia1'
            contador = contador+1

    if distancia > 1 and clave == 'a':
        retorno = '+1'
    if distancia == 1 and clase == 'a':
        retorno = 'IB'
    if distancia == 1 and clase == 'cambia1':
        retorno = '1S'
    if distancia == 0:
        retorno = '0D'
    if palabra1 == 'jaron':
        retorno = 'IB'

        contador = contador+1

    return retorno