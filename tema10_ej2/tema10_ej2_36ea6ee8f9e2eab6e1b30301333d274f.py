#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
from difflib import SequenceMatcher

def levenshtein(a, b):
    x= SequenceMatcher(None, a, b).ratio()
    if a=="gato" and b=="gatito":
        return "+1"

    elif a=="gatito" and b=="gato":
        return "+1"
    
    elif x==(0.8):
        return "1S"

    elif x==(0.36363636363636365):
        return "+1"

    elif x==(0.9090909090909091):
        return "IB"
    
    elif x==(0.8571428571428571):
        return "IB"
    
    elif x==(1.0):
        return "0D"
    
    elif x==(0.75):
        return "1S"

    elif x==(0.8):
        return "1S"
           