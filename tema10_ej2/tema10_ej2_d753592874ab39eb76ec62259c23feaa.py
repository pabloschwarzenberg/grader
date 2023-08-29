#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales

def levenshtein(palabra1,palabra2):
    
    if len(palabra1)==len(palabra2):
        i=0
        contador=0
        while i in range(len(palabra1)):
            if palabra1[i]!=palabra2[i]:
                contador+=1
            i+=1
                
        if contador==1:
            return ("1S")
        elif contador==0:
            return ("0D")

    else:
        if len(palabra1)>len(palabra2):
            lista=[]
            for letra in palabra1:
                if letra not in palabra2:
                    lista.append(letra)
                    uni=len(lista)
            if uni==1:
                return ("IB")
            elif uni>1:
                return ("+1")
            
        if len(palabra1)<len(palabra2):
            lista2=[]
            for letra in palabra2:
                if letra not in palabra1:
                    lista2.append(letra)
            uni2=len(lista2)
            if uni2==1:
                return ("IB")
            elif uni2>1:
                return ("+1")
            else:
                return ("IB")
                
if __name__=="__main__":
    pass
           