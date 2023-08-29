#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(x,y):
    if x==y:
        return "0D"
    if x!=y and len(x)==len(y):
        return("1S")
    if x!=y and len(x)==len(y)+1 or len(x)+1==len(y):
        return("IB")
    if len(x)<len(y) or len(x)>len(y):
        return("+1")
print(levenshtein("jaron","jarron"))
           