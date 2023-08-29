#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if not palabra1:
        return len(palabra2)
    if not palabra2:
        return palabra1
    return  min(
        levenshtein(palabra1[1:],palabra2[1:])+(palabra1[0]!=palabra2[0]),
        levenshtein(palabra1[1:],palabra2)+1,
        levenshtein(palabra1,palabra2[1:])+1
    )
   

           