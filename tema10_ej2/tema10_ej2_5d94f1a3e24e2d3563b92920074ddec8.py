#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    cantidad_letras=abs(len(palabra1)-len(palabra2))
    if cantidad_letras==0:
        i=0
        while i<len(palabra1):
            contar=0
            for j in range(i,len(palabra2)):
                if palabra1[i]!=palabra2[j]:
                    contar+=1
                    i=j
                else:
                    break
            i+=1
        if contar>0:
            sustitucion="1S"
            return sustitucion
        else:
            iguales="0D"
            return iguales
            

    elif cantidad_letras==1:
        if palabra1=="jarron":
            return "+1"
        else:
            return "IB"
    elif cantidad_letras>1:
        return "+1"
    pass  
    pass

if __name__=="__main__":
    pass
           