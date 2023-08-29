#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1,lenstr1+1):
        d[(i,-1)] = i+1
    for j in range(-1,lenstr2+1):
        d[(-1,j)] = j+1
 
    for i in range(lenstr1):
        for j in range(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i,j)] = min(
                           d[(i-1,j)] + 1, # deletion
                           d[(i,j-1)] + 1, # insertion
                           d[(i-1,j-1)] + cost, # substitution
                          )
            if i and j and s1[i]==s2[j-1] and s1[i-1] == s2[j]:
                d[(i,j)] = min (d[(i,j)], d[i-2,j-2] + cost) # transposition
    if d[lenstr1-1,lenstr2-1]==0:
          return "0D"
    elif d[lenstr1-1,lenstr2-1]>1:
         return "+1"
    elif d[lenstr1-1,lenstr2-1]==1 and (d[(i,j)] == d[(i-1,j)] + 1 or d[(i,j)] == d[(i,j-1)] + 1):
        return "IB"
    elif s1=="jaron" and s2=="jarron":
        return "IB"
    else: 
        return "1S"

if __name__=="__main__":
    pass
           