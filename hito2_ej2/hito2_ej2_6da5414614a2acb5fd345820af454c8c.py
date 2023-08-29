      def esSubstitucion(str1, str2):
    errores = 0
    i = 0
    while i < len(str1):
        if str1[i] != str2[i]:
            errores = errores + 1
def levenshtein(str1, str2):
    if str1 == str2:
        return '0D'
    elif len(str1) == len(str2):
        varSubs = esSubstitucion(str1, str2)
        if varSubs:
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




def esSubstitucion(str1, str2):
    errores = 0
    i = 0
    while i < len(str1):
        if str1[i] != str2[i]:
            errores = errores + 1
        i = i + 1
    return errores == 1

def esCambio(str1, str2):
def levenshtein(str1, str2):
    if str1 == str2:
        return '0D'
    elif len(str1) == len(str2):
        varSubs = esSubstitucion(str1, str2)
        if varSubs:
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






