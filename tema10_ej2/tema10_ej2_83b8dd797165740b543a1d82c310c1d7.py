#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(a, b):
    if a == b:
        return '0D'
    
    elif len(a) == len(b):
        return '1S'
    
    elif abs(len(a)-len(b)) == 1:
        
        for x in a:
            b = b.strip(x)
        
        if len(b) <= 1:
            return 'IB'
        else:
            return '+1'
       
        
    if abs(len(a)-len(b)) > 1:
        return '+1'

if __name__=="__main__":
    pass
           