#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def lala(s1, s2):
    if len(s1)<len(s2):
        return lala(s2,s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j+1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def levenshtein(s1, s2):
    if lala(s1, s2) == 0:
        return "0D"
    elif lala(s1, s2) == 1:
        if len(s1) == len(s2):
            return "1S"
        else:
            return "IB"
    elif lala(s1, s2) > 1:
        return"+1"

if __name__=="main_":

    s1 = input()
    s2 = input()
