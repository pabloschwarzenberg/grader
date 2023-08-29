#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    i=0
    q=0
    if len(palabra1) == len (palabra2):
        while i<len(palabra1):
            if palabra1[i] == palabra2[i]:
                q+=1
            i+=1
        if q == len(palabra1)-1:
            return "1S"
        if q == len(palabra1):
            return "0D"

    elif len(palabra1) == len(palabra2)+1 or len(palabra1)+1 == len(palabra2):
        if len(palabra2)>len(palabra1):
            k=palabra1
            palabra1=palabra2
            palabra2=k

        i=0
        q=0
        while i<len(palabra1):
            lista=list(palabra1)
            lista.pop(i)
            if "".join(lista) == palabra2:
                q+=1
                break
            i+=1
        if q==1:
            return "IB"
        if q==0:
            return "+1"    
    else:
        return "+1"



if __name__=="__main__":
    pass
           