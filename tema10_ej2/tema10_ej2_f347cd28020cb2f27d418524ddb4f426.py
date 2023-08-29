def esSubstitucion(palabra1, palabra2):

    errores = 0

    i = 0

    while i < len(palabra1):

        if palabra1[i] != palabra2[i]:

            errores = errores + 1

        i = i + 1

    return errores == 1
def esCambio(palabra1, palabra2):

    strAux = ""

    encontrada = False

    i = 0

    while i < len(palabra1) and not(encontrada):

        if palabra1[i] != palabra2[i]:

            encontrada = True

            strAux = strAux + palabra2[i + 1 : len(palabra2)]

        else:

            strAux = strAux + palabra2[i]

        i = i + 1

    return strAux == palabra1
    
def levenshtein(palabra1,palabra2):
    
    if palabra1 == palabra2:

        return "0D"

    elif len (palabra1) == len(palabra2):

        varSubs = esSubstitucion(palabra1, palabra2)

        if varSubs:

            return "1S"

        else:

            return "+1"

    elif (len(palabra1)-len(palabra2) == -1):

        if esCambio(palabra1, palabra2):

            return "IB"

        else:

            return "+1"

    elif (len(palabra1)-len(palabra2) == 1):

        if esCambio(palabra2, palabra1):

            return "1B"

        else:

            return"+1"

    else: return "+1"

print(levenshtein("jaron", "jarron"))