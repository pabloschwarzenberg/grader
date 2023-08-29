#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if palabra1 == palabra2:
        return "0D"
    else:
        counter = 0
        if len(palabra1) == len(palabra2):
            i = 0
            while i < len(palabra1):
                if palabra1[i] != palabra2[i]:
                    counter += 1
                i += 1
            if counter >= 2:
                return "+1"
            elif  counter == 1:
                return "1S"
        else:
            if abs(len(palabra1) - len(palabra2)) > 1:
                return "+1"
            else:
                if len(palabra1) > len(palabra2):
                    PM = palabra1
                    pm = palabra2
                else:
                    PM = palabra2
                    pm = palabra1
                PM = list(PM)
                for i in pm:
                    if i in PM:
                        a = PM.index(i)
                        PM.pop(a)
                if len(PM) == 1:
                    return "IB"
                else:
                    return "+1"