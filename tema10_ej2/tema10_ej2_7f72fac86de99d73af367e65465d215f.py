#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if palabra1 == palabra2:
        return "0D"
    if len(palabra1)==len(palabra2):
        return "1S"
    if len(palabra1)+1==len(palabra2) or (
       len(palabra1)-1==len(palabra2)):
        lista=[len(palabra1),len(palabra2)]
        i=0
        similar=0
        while i<min(lista):
            if palabra1[i]==palabra2[i]:
                similar+=1
            i+=1
        if similar>=3:
            return "IB"
        else:
            return "+1"
    else:
        return "+1"
    pass
           