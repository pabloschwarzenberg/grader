#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if palabra1==palabra2:
        return "0D"
    elif len(palabra1)==len(palabra2):
        i=0
        for letra in range(0,len(palabra1)):
            if palabra1[letra]==palabra2[letra]:
                i+=1
        if i==len(palabra1)-1:
            return "1S"
        else:
            return "+1"
    elif len(palabra1)!=len(palabra2):
        if len(palabra1)<len(palabra2) and len(palabra1)+1!=len(palabra2):
            return "+1"
        if len(palabra1)>len(palabra2) and len(palabra2)+1!=len(palabra1):
            return "+1"
        if len(palabra1)>len(palabra2):
            for letra in palabra1:
                if palabra1.count(letra)!=palabra2.count(letra):
                    if letra in palabra2 and palabra1.count(letra)==palabra2.count(letra)+1:
                        return "IB"
                    return "+1"
        if len(palabra2)>len(palabra1):
            for letra in palabra2:
                if palabra2.count(letra)!=palabra1.count(letra):
                    if letra in palabra1 and palabra2.count(letra)==palabra1.count(letra)+1:
                        return "IB"
                    return "+1"
        
        
        
        



if __name__=="__main__":
    pass
           