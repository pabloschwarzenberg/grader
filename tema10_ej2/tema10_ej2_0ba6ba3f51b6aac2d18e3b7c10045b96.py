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
        return "1S"
    elif palabra2!=palabra1:
        palabra1=list(palabra1)
        palabra2=list(palabra2)
        if len(palabra1)>len(palabra2):
            letras=[]
            for i in palabra1[:]:
                if i in palabra2:
                    palabra2.remove(i)      
                else:
                    letra=palabra1.pop(palabra1.index(i))
                    letras.append(letra)
            if len(letras)>1:
                return "+1"
            if len(letras)==1:
                return "IB"
        elif len(palabra2)>len(palabra1):
            letras=[]
            for i in palabra2[:]:
                if i in palabra1:
                    palabra1.remove(i)      
                else:
                    letra=palabra2.pop(palabra2.index(i))
                    letras.append(letra)
            if len(letras)>1:
                return "+1"
            if len(letras)==1:
                return "IB"
    
    pass

if __name__=="__main__":
    pass
           