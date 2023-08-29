#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    contador=0
    if palabra1==palabra2:
        return "0D"
    else:
        if len(palabra1)==len(palabra2):
            contador=0
            for i in range(len(palabra1)):
                if palabra1[i]!=palabra2[i]:
                    contador+=1
        else:
            z=list(palabra2)
            for i in range(len(palabra1)):
                if palabra1[i] in z:
                    z.remove(palabra1[i])
            if abs(len(palabra1)-len(palabra2))==len(z):
                print ("Agregue/quite: ", len(z), "caracteres")
            else:
                print ("Operacion mixta")
        if contador==1:
            return "1S"
        elif len(z)==1:
            return "IB"
        elif contador>1 or len(z)>1:
            return "+1"
   

if __name__=="__main__":
    pass
           