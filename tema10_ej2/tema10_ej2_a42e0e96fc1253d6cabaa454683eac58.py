#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if len(palabra1)==len(palabra2):
        if palabra1==palabra2:
            resultado="0D"
        else:
            resultado="1S"
        
    elif len(palabra1)!=len(palabra2):
        if len(palabra1)>(len(palabra2)+1):
            resultado="+1"
        elif len(palabra2)>(len(palabra1)+1):
            resultado="+1"
        elif palabra1[0]!=palabra2[0]:
            resultado="+1"
        else:
            resultado="IB"
    
    return resultado


if __name__=="__main__":
    palabra1=input("Ingrese palabra 1:")
    palabra2=input("Ingrese palabra 2:")
    print(levenshtein(palabra1,palabra2))
           