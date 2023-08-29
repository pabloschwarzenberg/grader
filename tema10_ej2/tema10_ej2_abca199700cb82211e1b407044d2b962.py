#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
   if len(palabra1) < len(palabra2):
        return levenshtein(palabra2, palabra1)

   if len(palabra2) == 0:
        return len(palabra1)

   pe = range(len(palabra2) + 1)
   for i, c1 in enumerate(palabra1):
       pa = [i + 1]
       for j, c2 in enumerate(palabra2):
           co = pe[j + 1] + 1
           de = pa[j] + 1
           su = pe[j] + (c1 != c2)
           pa.append(min(co, de, su))
       pe = pa
       

   return pe[-1]
           