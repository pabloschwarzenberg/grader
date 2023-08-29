#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    cont = 0
    cont2 = 0
    for i in palabra1:
        if i != "":
            cont +=1
    for i in palabra2:
        if i != "":
            cont2 +=1
    if cont -cont2 == 0:
        return "0D"
    elif cont - cont2 > 1 or cont2 - cont > 1:
        return "+1"
    if cont > cont2:
        a = cont - cont2
        if a == 1:
            return "IB"
    elif cont2> cont:
        a = cont2 - cont
        if a == 1:
            return "IB"

if __name__=="__main__":
    pass
           
           