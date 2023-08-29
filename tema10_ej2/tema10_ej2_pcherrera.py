def levenshtein(palabra1,palabra2):
    if len(palabra1) < len(palabra2):
        #es necesario agregar veamos si es mas de una letra
        if len(palabra2)-len(palabra1) > 1:
            return "+1"
        elif len(palabra2)-len(palabra1) == 1:
            i = 0
            for c in palabra1 :
                if palabra2.find(c) == -1:
                #si una letra no esta en palabra2 agregamos 1 al contador
                    i +=1
                if i > 1 :
                    #si i > 1 esto quiere decir que falta mas de una letra
                    return "+1"
                else :
                    return "IB"

    elif len(palabra1) == len(palabra2):
        i = 0
        for c in palabra1 :
            if palabra2.find(c) == -1 :
                i +=1
        if i > 1 :
            return +1
        else:
            if palabra1 == palabra2 :
                return "0D"
            else :
                return "1S"
    else :
        #es necesario quitar una borra una letra veamos si es mas de una letra
        if len(palabra1)-len(palabra2) > 1:
            return "+1"
        elif len(palabra1)-len(palabra2) == 1:
            i = 0
            for c in palabra2 :
                if palabra1.find(c) == -1:
                #si una letra no esta en palabra2 agregamos 1 al contador
                    i +=1
            if i > 1 :
                    #si i > 1 esto quiere decir que falta mas de una letra
                    return "+1"
            else :
                    return "IB" 
    

if __name__=="__main__":
    pass