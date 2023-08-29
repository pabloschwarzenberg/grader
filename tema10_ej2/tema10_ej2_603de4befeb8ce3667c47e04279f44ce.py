def levenshtein(palabra1,palabra2):
    lista1 = list(palabra1)
    lista2 = list(palabra2)
    igualdad = 0
    if palabra1 == palabra2:
        return "0D"    
    if palabra1 != palabra2 and (len(palabra1) - len(palabra2)) >= 2 or (len(palabra2) - len(palabra1)) >= 2:
        return "+1"
    if ((len(palabra1) - len(palabra2)) == 1 or (len(palabra2) - len(palabra1)) == 1) and lista1[0] == lista2[0]:
        return "IB"     
    if len(palabra1) != len(palabra2):
        for i in range(min(len(lista1),len(lista2))):
            if lista1[i] != lista2[i]:
                return "+1" 
    
    if len(palabra1) == len(palabra2): 
        for i in range(len(palabra1)):
            if lista1[i] == lista2[i]:
                igualdad = igualdad + 1
        if igualdad == (len(palabra1)-1):
            return "1S" #sustituir
