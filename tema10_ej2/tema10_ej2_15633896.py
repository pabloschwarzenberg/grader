#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if palabra1==palabra2:
        
        return "0D"

    elif len(palabra1)==len(palabra2):
        contador=0
        for cada_letra in range(len(palabra1)):
            if palabra1[cada_letra]==palabra2[cada_letra]:
                contador=contador

            else:
                contador=contador+1
        if contador ==1:
            return "1S"
        else:
            return "+1"

    elif len(palabra1)>len(palabra2):
        diferencia=len(palabra1)-len(palabra2)

        cambios=0

        for i in range (len(palabra2)):
            if palabra1[i]==palabra2[i]:
                cambios= 1

            else:
                for i in range(len(palabra2)):
                    if palabra1[i]!=palabra2[i]:
                        a=list(palabra1)
                        a.pop(i)
                        if palabra2=="".join(a):
                            cambios=1
                        else:
                            cambios=2
                        break
                            
        if diferencia==1 and cambios==1:
            return "IB"
        else:
            return "+1"
            
            

    elif len(palabra2)>len(palabra1):
        diferencia=len(palabra2)-len(palabra1)

        cambios=0
        
        for i in range (len(palabra1)):
            if palabra1[i]==palabra2[i]:
                cambios= 1

            else:
                cambios=0
                for i in range(len(palabra1)):
                    if palabra1[i]!=palabra2[i]:
                        a=list(palabra2)
                        a.pop(i)
                        if palabra1=="".join(a):
                            cambios=1
                        else:
                            cambios=2

                        break
                    
        if diferencia==1 and cambios==1:
            return "IB"

        else:
            return "+1"
 
            
            

    
print(levenshtein("jarron","jaron")) 
if __name__=="__main__":
    pass
           