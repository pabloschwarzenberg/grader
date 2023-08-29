# La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1, palabra2):
    if palabra1==palabra2:
        return "0D"
    elif len(palabra1)>len(palabra2)+1 or len(palabra2)>len(palabra1)+1:
        return "+1"
    elif len(palabra1)==len(palabra2)+1 or len(palabra2)==len(palabra1)+1:
        if len(palabra1)>len(palabra2):
            for x in range(len(palabra1)):
                if palabra1[:x]+palabra1[x+1:]==palabra2:
                    return "IB"
        elif len(palabra2)>len(palabra1):
            for y in range(len(palabra2)):
                if palabra2[:y]+palabra2[y+1:]==palabra1:
                    return "IB"

        return "+1"
    elif len(palabra1)==len(palabra2):
        n=0
        for i in range(len(palabra1)):
            if palabra1[i]!=palabra2[i]:
                n+=1
        if n==1:
            return "1S"
        else:
            return "+1"

if __name__ == "__main__":
    palabra1=input("palabra1: ")
    palabra2=input("palabra2: ")
    print(levenshtein(palabra1,palabra2))
    pass


