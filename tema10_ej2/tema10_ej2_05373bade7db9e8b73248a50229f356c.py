#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales

def lala(palabra1, palabra2):
    if len(palabra1)<len(palabra2):
        return lala(palabra2,palabra1)

    if len(palabra2) == 0:
        return len(palabra1)

    previous_row = range(len(palabra2) + 1)
    for i, c1 in enumerate(palabra1):
        current_row = [i + 1]
        for j, c2 in enumerate(palabra2):
            insertions = previous_row[j+1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def levenshtein(palabra1, palabra2):
    if lala(palabra1, palabra2) == 0:
        return "0D"
    elif lala(palabra1, palabra2) == 1:
        if len(palabra1) == len(palabra2):
            return "1S"
        else:
            return "IB"
    elif lala(palabra1, palabra2) > 1:
        return"+1"


if __name__=="__main__":
    palabra1=input()
    palabra2=input()
    pass
           