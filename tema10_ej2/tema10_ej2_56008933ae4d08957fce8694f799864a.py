#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales

def levenshtein(palabra1,palabra2):
    palabra_1=list(palabra1)
    palabra_2=list(palabra2)   
    if len(palabra1)==len(palabra2):
        contador=0
        for j in range(len(palabra_1)):
            if palabra_1[j]!=palabra_2[j]:
               contador=contador+1
            else:
                contador=contador
        if contador>1:
           return "+1"
        elif contador==1:
           return "1S"
        else:
           return "0D"
    elif abs(len(palabra1)-len(palabra2))==1:
        if len(palabra1)>len(palabra2):
            mayor=palabra1
            menor=palabra2
        else:
            mayor=palabra2
            menor=palabra1
        pa1=list(mayor)
        pa2=list(menor)
        i=0
        c=0
        while i<len(menor) and c<len(pa1):
            if pa1[c]==pa2[i]:
                pa1.remove(pa1[c])
                i+=1
            else:
                c+=1
        if len(pa1)==1:
            return "IB"
        else:
            return "+1"
    else:
     return "+1"

        
