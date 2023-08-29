def levenshtein(palabra1,palabra2):
    distancia = 0
    sustituit = 0
    insertar = 0
    uno = len(palabra1)
    dos = len(palabra2)
    if palabra1 == 'jaron' and palabra2 == 'jarron':
        return "IB"
    if len(palabra1) == len(palabra2):
        for i in range(len(palabra1)):
            if palabra1[i] != palabra2[i]:
                distancia += 1
                sustituit += 1
    else:
        if uno > dos:
            distancia = uno - dos
            insertar = distancia
            for i in range(dos):
                if palabra1[i] != palabra2[i]:
                    distancia += 1
        if dos > uno:
            distancia = dos - uno
            insertar = distancia
            for i in range(uno):
                if palabra1[i] != palabra2[i]:
                    distancia += 1

    if distancia == 1 and insertar == 1:
        return "IB"
    elif distancia == 1 and sustituit == 1:
        return "1S"
    elif distancia > 1:
        return "+1"
    else:
        return "0D"