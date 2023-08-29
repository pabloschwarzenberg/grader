def levenshtein(palabra1,palabra2):
    if len(palabra1) < len(palabra2):
         mayor = palabra2
         menor = palabra1
    else:
        mayor = palabra1
        menor = palabra2

    distancia = len(mayor) - len(menor)

    if distancia >= 1:
        respuesta = "+1"

    elif distancia == 0 and palabra1 != palabra2:
        respuesta = "1S"

    elif distancia == 0 and palabra1 == palabra2:
        respuesta = "0D"

    elif palabra1 != palabra2 and distancia != 0:
        respuesta = "IB"
    return(respuesta)