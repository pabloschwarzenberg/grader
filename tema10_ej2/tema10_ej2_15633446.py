#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
import math
def levenshtein(palabra1,palabra2):
    if len(palabra1)!=len(palabra2):
        r=math.fabs(len(palabra1)-len(palabra2))
        if r>1:
            return "+1"
        elif r==1:
            if palabra1 in palabra2 or palabra2 in palabra1:
                return "IB"
            else:
                for j in range(min(len(palabra1),len(palabra2))):
                    if palabra1[j]==palabra2[j]:
                        continue
                    elif palabra1[j]==palabra2[j+1]:
                        continue
                    elif palabra2[j]==palabra1[j+1]:
                        continue
                    else:
                        return"+1"
                return "IB"
                    
                
    else:   
        r=0
        for i in range(len(palabra1)):
            if palabra1[i]==palabra2[i]:
                continue
            else:
                r=r+1
        if r==0:
            return "0D"
        if r==1:
            return "1S"
        if r>1:
            return "+1"
     
    pass
if __name__=="__main__":
    pass
           