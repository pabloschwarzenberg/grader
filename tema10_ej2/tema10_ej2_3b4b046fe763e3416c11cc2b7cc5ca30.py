#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    palabra_2=[]
    letras_iguales=0
    if palabra1==palabra2:
        return '0D'
    for i in palabra2:
        palabra_2.append(i)
    for i in palabra1:
        if i in palabra_2:
            letras_iguales+=1
            palabra_2.remove(i)
    if len(palabra1)==len(palabra2) and len(palabra2)-letras_iguales==1:
        return '1S'
    if len(palabra1)<len(palabra2):
        leven=len(palabra2)-letras_iguales
    else:
        leven=len(palabra1)-letras_iguales
    if leven>1:
        return '+1'
    elif leven==1:
        return 'IB'
if __name__=="__main__":
    pass
           