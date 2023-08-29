#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    distancia_mayor="+1"
    insertar_o_borrar="IB"
    sustituir="1S"
    iguales="0D"
    diferencia=0
    if palabra1==palabra2:
        return iguales
    elif len(palabra1)==len(palabra2):
        return sustituir
    elif len(palabra1)==len(palabra2)+1:
        for i in range(len(palabra1)):
            if palabra1[i] not in palabra2:
                diferencia+=1
        for i in range(len(palabra1)-len(palabra2)):
                diferencia+=1
                i+=1
        if diferencia==1:
            return insertar_o_borrar
        if diferencia>1:
            return distancia_mayor
    elif len(palabra1)+1==len(palabra2):
        for i in range(len(palabra2)):
            if palabra2[i] not in palabra1:
                diferencia+=1
        for i in range(len(palabra2)-len(palabra1)):
                diferencia+=1
                i+=1
        if diferencia==1:
            return insertar_o_borrar
        if diferencia>1:
            return distancia_mayor
                       
    else:
        return distancia_mayor
           