import math

def levenshtein(a,b):
    lista=list(a)
    listb=list(b)
    aux=listb.copy()
    if lista==listb:
        return '0D'
    elif abs(len(lista)-len(listb))>1:
        return'+1'
    elif abs(len(lista)-len(listb))<=1:
        if abs(len(lista)-len(listb))<=1 and abs(len(lista)-len(listb))>=0:
            for i in range(len(aux)):
                if aux[i] in lista:
                    a=aux[i]
                    listb.remove(a)
                    lista.remove(a)
            if (len(lista)==1 and len(listb)==0) or (len(lista)==0 and len(listb)==1):
                return'IB'
            elif len(lista)==1 and len(listb)==1:
                return'1S'
            else:
                return'+1'



           