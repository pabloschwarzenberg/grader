#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    
     a=len(palabra1)-len(palabra2)
     p_1=list(palabra1)
     p_2=list(palabra2)
     b=""
     if a>1 or a<1 :
       b="+1"
     elif a==1: 
       b="IB"
     elif p_1==p_2:
        b="OD"
     elif a==0:
       b="1S"
    return b

if __name__=="__main__":
    pass
           