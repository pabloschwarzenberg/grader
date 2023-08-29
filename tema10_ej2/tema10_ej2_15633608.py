#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if palabra1 == palabra2:
        return "0D"
    for i in palabra1:
        for e in palabra2:
            spa=palabra1.split(i,1)
            spb=palabra2.split(e,1)
            if e.join(spa)==palabra2 or i.join(spb)==palabra1:
                return "1S"
    for i in palabra1:
        for e in palabra2:
            spa=palabra1.split(i,1)
            spa="".join(spa)
            spb=palabra2.split(e,1)
            spb="".join(spb)
            if spa==palabra2 or spb==palabra1:
                return "IB"
    return "+1"

if __name__=="__main__":
    pass
           