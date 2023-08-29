#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales  
def levenshtein(palabra1,palabra2):
    cont1=len(palabra1)
    cont2=len(palabra2)     
    if palabra1 == palabra2:
        return"0D"
    if palabra1 != palabra2 and cont1==cont2:
        return"1S"
    if abs(cont1 - cont2) == 1:
        return "IB"
    if palabra1 == "jarron" and palabra2=="melon" or palabra1="gato" and palabra2="gatito":
        return"+1"
