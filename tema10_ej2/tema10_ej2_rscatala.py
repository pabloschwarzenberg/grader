#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    if len(palabra1) == len(palabra2):
        contador = 0
        for i in range(len(palabra1)):
            if palabra1[i] in palabra2:
                contador += 1
            else:
                continue
        if contador == len(palabra2):
            return "0D"
        elif len(palabra2)-contador == 1:
            return "1S"
        else:
            return "+1"
    else:
        if len(palabra1)<len(palabra2):
            contador = 0
            for i in range(len(palabra1)):
                if palabra1[i] in palabra2:
                    contador += 1
                else:
                    continue
            if len(palabra2)-contador == 1:
                return "IB"
            else:
                return "+1"
        else:
            contador = 0
            for i in range(len(palabra2)):
                if palabra2[i] in palabra1:
                    contador += 1
                else:
                    continue
            if len(palabra1)-contador == 1:
                return "IB"
            else:
                return "+1"
 

if __name__=="__main__":
    print(levenshtein("gato","pato"))
    print(levenshtein("pato","patito"))
           