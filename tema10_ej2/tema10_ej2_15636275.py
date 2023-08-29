#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if abs(len(palabra1)-len(palabra2))>1:
        return "+1"
    else:
        if len(palabra1)+1==len(palabra2):
            for i in range(len(palabra1)):
                if palabra1[i]!=palabra2[i]:
                    if palabra1[i:len(palabra1)]==palabra2[i+1:len(palabra2)]:
                        return "IB"
                    else:
                        return "+1"
            if palabra1==palabra2[0:len(palabra1)]:
                return "IB"
        elif len(palabra2)+1==len(palabra1):
            for i in range(len(palabra2)):
                if palabra2[i]!=palabra1[i]:
                    if palabra2[i:len(palabra2)]==palabra1[i+1:len(palabra1)]:
                        return "IB"
                    else:
                        return "+1"
            if palabra2==palabra1[0:len(palabra2)]:
                return "IB"
        elif len(palabra2)==len(palabra1):
            for i in range(len(palabra1)):
                if palabra1[i]!=palabra2[i]:
                    if palabra1[i+1:len(palabra1)]==palabra2[i+1:len(palabra2)]:
                        return "1S"
                    else:
                        return "+1"
            return "0D"