#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if palabra1==palabra2:
        return "0D"
    if len(palabra1)==len(palabra2):
        contador=0
        palabra11=list(palabra1)
        palabra22=list(palabra2)
        for n in palabra11:
            if n not in palabra22:
                contador+=1
        if contador==1:
            return "1S"
        else:
            return "+1"
    if len(palabra1)!=len(palabra2):
        y=len(palabra1)
        x=len(palabra2)
        if x>y:
            contador=x-y
        else:
            contador=y-x
        palabra11=list(palabra1)
        palabra22=list(palabra2)
        for n in palabra11:
            if n not in palabra22:
                contador+=1
        if contador==1:
            return "IB"
        else:
            return "+1"       
    pass

if __name__=="__main__":
    pass

