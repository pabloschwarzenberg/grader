def levenshtein(palabra1, palabra2):
    contador = 0
    if palabra1 == palabra2:
        return "0D"
    elif len(palabra1) > len(palabra2) + 1:
        return "+1"
    elif len(palabra2) > len(palabra1) + 1:
        return "+1"
    elif len(palabra1) == len(palabra2):
        for i in range(len(palabra1)):
            if palabra1[i] != palabra2[i]:
                contador += 1
        if contador > 1:
            return "+1"
        elif contador == 1:
            return "1S"
    elif len(palabra1) == len(palabra2) + 1:
        for i in range(len(palabra2)):
            if palabra1[i] != palabra2[i]:
                contador += 1
        if contador > 0:
            return "+1"
        elif contador == 0:
            return "IB"



    elif len(palabra2) == len(palabra1) + 1:
        
            return "IB"

   
    
           
