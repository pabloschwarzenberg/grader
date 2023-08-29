#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    n = abs(len(palabra1) - len(palabra2))
    if n > 1:
        return '+1'
    
    elif n == 1:
        return 'IB'
        
    elif n == 0:
        if palabra1 != palabra2:
            return '1S'
            
        else:
            return '0D'

if __name__=="__main__":

    pass
           