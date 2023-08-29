#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if len(palabra1) - len(palabra2) > 1 or len(palabra2) - len(palabra1) > 1:
        return '+1'
    
    elif palabra1 == palabra2:
        return '0D'
    
    elif len(palabra1) - len(palabra2) == 1 or len(palabra2) - len(palabra1) == 1:
        return 'IB'
    
    elif len(palabra1) - len(palabra2) == 0 or len(palabra2) - len(palabra1) == 0:
        return '1S'

if __name__=="__main__":
    pass
           