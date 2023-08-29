#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    cont=0
    maximo=float("-inf")
    l1=len(palabra1)
    if l1>maximo:
        maximo=l1
    l2=len(palabra2)
    l1=len(palabra1)
    if l2>maximo:
        maximo=l2
    for letra in palabra1:
        if letra in palabra2:
            cont+=1
    valor=maximo-cont
    if valor>1:
        return "+1"
    elif valor==1 and l1!=l2:
        return "IB"
    elif valor==1 and l1==l2:
        return "1S"
    else:
        return "0D"

if __name__=="__main__":
    print(levenshtein("colas","ola"))
    pass
           
