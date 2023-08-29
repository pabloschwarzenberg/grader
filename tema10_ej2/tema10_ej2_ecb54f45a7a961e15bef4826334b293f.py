#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
import cmath
def levenshtein(palabra1,palabra2):
    a=list(palabra1)
    b=list(palabra2)
    if abs((len(a)-len(b)))>1 or a[1]!=b[1]:
        return("+1")
    elif abs((len(a)-len(b)))==0:
        if palabra1==palabra2:
            return("0D")
        elif palabra1!=palabra2:
            return("1S")
    elif abs((len(a)-len(b)))==1 and a[0]==b[0]:
        return("IB")


if __name__=="__main__":
    pass
           