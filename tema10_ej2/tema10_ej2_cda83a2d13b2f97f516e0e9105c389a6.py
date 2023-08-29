def levenshtein(s1,s2) :
    if s1 == s2 :
        return "0D"
    lista1 = list(s1)
    lista2 = list(s2)
    contador = 0
    if len(s1) < len(s2) :
        for letra1 in lista1 :
            if letra1 != lista2[0] and letra1 in lista2 == True :
                lista1.remove(letra1)
                lista2.remove(letra1)
            elif letra1 != lista2[0]  :
                contador += 1
                lista1.pop(0)
                lista2.pop(0)
            else :
                lista1.pop(0)
                lista2.pop(0)
        contador = contador + len(lista2)
        if contador == 1 :
            return "1B"
    elif  len(s1) > len(s2) :
        for letra2 in lista2 :
            if letra2 != lista1[0] and letra2 in lista1 == True :
                lista1.remove(letra2)
                lista2.remove(letra2)
            elif letra2 != lista1[0] :
                contador += 1
                lista1.pop(0)
                lista2.pop(0)
            else :
                lista1.pop(0)
                lista2.pop(0)
        contador = contador + len(lista1)
        if contador == 1 :
            return "1B"
    elif  len(s1) == len(s2) :
        for letra1 in lista1:
            if letra1 != lista2[0] and letra1 in lista2 == True:
                contador += 1
                lista1.remove(letra1)
                lista2.remove(letra1)
            elif letra1 != lista2[0]:
                contador += 1
                lista1.pop(0)
                lista2.pop(0)
            else :
                lista1.pop(0)
                lista2.pop(0)
        if contador == 1:
            return "1S"
    if contador > 1 :
        return "+1"