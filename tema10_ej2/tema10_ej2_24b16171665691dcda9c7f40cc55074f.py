#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales

def levenshtein(palabra1,palabra2):

    valor1 = len(palabra1)
    
    valor2 = len(palabra2)
    
    total = valor1 -valor2
    
    if total < -1 or total >= 1 :
        return "+1"
        
    if total == 1 or total == -1 :
        return "IB"

    if total == 0  :
    
        if palabra1 == palabra2 :
            return "0D"
        else:
            return "1S"
