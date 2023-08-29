#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def esSubstitucion(str1,str2):
    errores = 0
    i = 0
    while i < len(str1):
        if str1[i] != str2[i]:
            errores = errores + 1
        i = i + 1
    return errores ==1

def esCambio(str1,str2):
    strAux = ''
    encontrada = False
    i = 0
    while i < len(str1) and not (encontrada):
        if str1[i] != str2[i]:
            encontrada = True
            strAux = strAux + str2[i + 1 : len(str2)]
        else:
            strAux = strAux + str2[i]
        i = i + 1
    return strAux == str1

def levenshtein(str1,str2):
    if str1 == str2:
        return  'OD'
    elif len(str1) == len(str2):
        varSubs = esSubstitucion(str1,str2)
        if varSubs:
            return 'ls'
        else:
            return '+1'
    elif (len(str1)-len(str2) == -1):
        if esCambio(str1,str2):
            return 'IB'
        else:
            return '+1'
    elif (len(str1)-len(str2) == 1):
        if esCambio(str2,str1):
            return 'IB'
        else:
            return '1+'
    else:
        return '+1'

print(levenshtein("jaron", "jarron"))
           