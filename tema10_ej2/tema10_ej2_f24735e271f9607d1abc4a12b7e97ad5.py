#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    pass

if __name__=="__main__":
    pass
def levenshtein(palabra1, palabra2):
    if palabra1 == palabra2:
        return "0D"

    len1, len2 = len(palabra1), len(palabra2)

    if abs(len1 - len2) > 1:
        return "+1"

    if len1 > len2:
        palabra1, palabra2 = palabra2, palabra1
        len1, len2 = len2, len1

    for i in range(len1):
        if palabra1[i] != palabra2[i]:
            if len1 == len2:
                return "1S"
            else:
                if palabra1[i:] == palabra2[i+1:]:
                    return "IB"
                else:
                    return "+1"

    return "IB"

if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")

    resultado = levenshtein(palabra1, palabra2)
    print(resultado)           