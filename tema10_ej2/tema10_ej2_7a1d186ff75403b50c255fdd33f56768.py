#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def esSubstitucion(str1, str2):
    error = 0
    letra = 0
    while letra < len(str1):
        if str1[letra] != str2[letra]:
            error = error + 1
        letra = letra + 1
    return error == 1

def esCambio(str1, str2):
    Aux = ''
    encontrada = False
    letra = 0
    while letra < len(str1) and not(encontrada):
        if str1[letra] != str2[letra]:
            encontrada = True
            Aux = Aux + str2[letra + 1 : len(str2)]
        else:
            Aux = Aux + str2[letra]
        letra = letra + 1
    return Aux == str

def levenshtein(str1, str2):
    if str1 == str2:
        return '0D'
    elif len(str1) == len(str2):
        Cambio = esSubstitucion(str1, str2)
        if Cambio:
            return '1S'
        else:
            return '+1'
    elif (len(str1)-len(str2) == -1):
        if esCambio(str1, str2):
            return 'IB'
        else:
            return '+1'
    elif (len(str1)-len(str2) == 1):
        if esCambio(str2, str1):
            return 'IB'
        else:
            return '+1'
    else:
        return '+1'