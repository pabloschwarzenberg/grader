def levenstain(palabra1, palabra2):
    error = 0
    i = 0
    while i < len(palabra1):
        if palabra1[i] != palabra2[i]:
            error = error + 1
        i = i + 1
    return error == 1

def cambiar(palabra1, palabra2):
    aux = ''
    a = False
    i = 0
    while i < len(palabra1) and not(a):
        if palabra1[i] != palabra2[i]:
            a = True
            aux = aux + palabra2[i + 1 : len(palabra2)]
        else:
            aux = aux + palabra2[i]
        i = i + 1
    return aux == palabra1
def levenshtein(palabra1, palabra2):
    if palabra1 == palabra2:
        return "0D"
    elif len(palabra1) == len(palabra2):
        variable = levenstain(palabra1, palabra2)
        if variable:
            return "1S"
        else:
            return "+1"
    elif (len(palabra1)-len(palabra2) == -1):
        if cambiar(palabra1, palabra2):
            return "IB"
        else:
            return '+1'
    elif (len(palabra1)-len(palabra2) == 1):
        if cambiar(palabra2, palabra1):
            return "IB"
        else:
            return "+1"
    else:
        return "+1"