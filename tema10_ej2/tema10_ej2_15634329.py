#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if len(palabra1)==len(palabra2):
        if palabra1==palabra2:
            return "0D"
        else:
            A=list(palabra1)
            B=list(palabra2)
            s=0
            for i in range(len(palabra1)):
                if A[i]!=B[i]:
                  s+=1
            if s==1:
                return "1S"
            else:
                return "+1"
    elif abs(len(palabra1)-len(palabra2))==1:
        if len(palabra2)<len(palabra1):
            A=palabra1
            palabra1=palabra2
            palabra2=A
        i=j=s=0
        while i<(len(palabra1)-1):
            if palabra1[i]!=palabra2[j]:
                if j==i:
                    j+=1
                else:
                    j+=1
                    i+=1
                s+=1
            else:
                j+=1
                i+=1
        if s==1:
             return "IB"
        else:
             return "+1"
         
    
    else:
        return "+1"
    pass

if __name__=="__main__":
    pass
           