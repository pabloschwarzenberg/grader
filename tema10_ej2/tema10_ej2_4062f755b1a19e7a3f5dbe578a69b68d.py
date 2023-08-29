#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    a = len(palabra1)
    b = len(palabra2)
    if (a + 1 == b or a == b + 1) and (palabra1[:1] == palabra2[:1]):
        return ("IB")
    elif a == b and palabra1 != palabra2:
        return ("1S")
    elif a == b and palabra1 == palabra2:
        return ("0D")
    else:
        return ("+1")
    pass

if __name__=="__main__":
    levenshtein()
    pass
           