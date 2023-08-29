#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    a=palabra1
    b=palabra2
    if a == b:
        return "0D"
    for i in a:
        for e in b:
            spa=a.split(i,1)
            spb=b.split(e,1)
            if e.join(spa)==b or i.join(spb)==a:
                return "1S"
    for i in a:
        for e in b:
            sppa=a.split(i,1)
            spa="".join(sppa)
            sppb=b.split(e,1)
            spb="".join(sppb)
            if spa==b or spb==a:
                return "IB"
    return "+1"


if __name__=="__main__":
    pass
           