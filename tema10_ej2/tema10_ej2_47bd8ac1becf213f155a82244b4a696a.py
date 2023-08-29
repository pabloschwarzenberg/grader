#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    distancia=[]
    if len(palabra1)==len(palabra2):
        for i in palabra1:
            if i!=palabra2[palabra1.index(i)]:
                distancia.append(i)
        if len(distancia)==0:
            return "0D"
        elif len(distancia)==1:
            return "1S"
        elif len(distancia)>1:
            return "+1"
    elif len(palabra1)-len(palabra2)>1 or len(palabra2)-len(palabra1)>1:
        return "+1"
    elif len(palabra1)-len(palabra2)==1:
        for i in palabra2:
            if i not in palabra1:
                distancia.append(i)
        if len(distancia)>0:
            return"+1"
        elif len(distancia)==0:
            return "IB"
    elif len(palabra2)-len(palabra1)==1:
        for i in palabra1:
            if i not in palabra2:
                distancia.append(i)
        if len(distancia)>0:
            return"+1"
        elif len(distancia)==0:
            return "IB"
    
if __name__=="__main__":
    print("Ejemplos:")
    print(levenshtein("gato","gatito"))
    print(levenshtein("hola","ola"))
    print(levenshtein("gallina","gallina"))
    print(levenshtein("caro","cara"))
    palabra1=input("___________________\nPalabra 1: ")
    palabra2=input("Palabra 2: ")
    print(levenshtein(palabra1,palabra2))