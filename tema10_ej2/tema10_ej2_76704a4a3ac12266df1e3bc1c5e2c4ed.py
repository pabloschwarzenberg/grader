#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    p=0
    i=0
    if len(palabra1)==len(palabra2):
        while p <= len(palabra1)-1:
            if palabra1[i]==palabra2[i]:
                i=i+1
            p+=1
        if p==i:
          return "0D"
        elif p>i:
          return "1S"
    else:
        if (len(palabra1)-len(palabra2)==1 or len(palabra2)-len(palabra1)==1) and palabra1[0]==palabra2[0] :
            return "IB"
        elif len(palabra1)-len(palabra2)>1 or len(palabra2)-len(palabra1)>1 or (palabra1[0]!=palabra2[0] and palabra1[0]!=palabra2[0]):
            return "+1"

if __name__=="__main__":
    pass
           