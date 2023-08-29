#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    palabra1.strip()
    palabra2.strip()
    palabra1_1 = []
    palabra2_2 = []
    for letra in palabra1:
        palabra1_1.append(letra)
    for letra in palabra2:
        palabra2_2.append(letra)
    if palabra1==palabra2:
        distancia_Levenshtei=0
        return "0D"
    else:
        if len(palabra1)>len(palabra2)+1 or len(palabra2)>len(palabra1)+1:
            return "+1"
        elif len(palabra1)==len(palabra2):
            for i in range(len(palabra1)):
                if palabra1_1[i]!=palabra2_2[i]:
                    palabra1_1[i]=palabra2_2[i]
                    if palabra1_1 == palabra2_2:
                        return "1S"
                    else:
                        return "+1"
                        
        else:
            if len(palabra2_2)>len(palabra1_1):
                for i in range(len(palabra1_1)):
                    if palabra1_1[i] != palabra2_2[i]:
                            palabra2_2.remove(palabra2_2[i])
                            if palabra2_2==palabra1_1:
                                return "IB"
                            else:
                                return "+1"
            elif len(palabra1_1)>len(palabra2_2):
                for i in range(len(palabra2_2)):
                    if palabra1_1[i] != palabra2_2[i]:
                        palabra1_1.remove(palabra1_1[i])
                        if palabra2_2 == palabra1_1:
                            return "1B"


if __name__=="__main__":
    palabra1 = "hola"
    palabra2 = "ola"
    levenshtein(palabra1,palabra2)
           