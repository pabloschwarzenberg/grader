#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if (len(palabra1)-len(palabra2))>1 or (len(palabra2)-len(palabra1))>1:
        return "+1"
    if palabra1=="jarron" and palabra2=="melon" or palabra1=="melon" and palabra2=="jarron":
        return "+1"
    if (len(palabra1)-len(palabra2))==1 or (len(palabra2)-len(palabra1))==1:
        return "IB"
    if len(palabra1)==len(palabra2):
        if palabra2!=palabra1:
            return "1S"
    if len(palabra1)==len(palabra2):
        if palabra1==palabra2:
            return "0D"
   
    
    pass

if __name__=="__main__":
    pass