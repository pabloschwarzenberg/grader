#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    a=0
    b=0
    c=0
    if len(palabra1)< len(palabra2):
        for i in palabra1:
            for f in palabra2:
                if i ==f:
                    a+=1
        c=a+(len(palabra1)-len(palabra2))
    elif len(palabra2)< len(palabra1):
        for i in palabra2:
            for f in palabra1:
                if i ==f:
                    a+=1
                else:
                    b+=1
        c=a+(len(palabra2)-len(palabra1))
    
    elif palabra1==palabra2:
       return "0D"
    if a>0:
        return "+1"
    if a==0 and c==1:
        return ("1B")
    elif b==1 and c==0:
        return("1S")

if __name__=="__main__":
    pass
       

           