#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1, palabra2):
    if palabra1 == palabra2:
        return "0D"
    
    len1, len2 = len(palabra1), len(palabra2)
    
    if abs(len1 - len2) > 1:
        return "+1"
    
    if len1 == len2:
        distance = sum(a != b for a, b in zip(palabra1, palabra2))
        if distance == 1:
            return "1S"
    
    if len1 > len2:
        palabra1, palabra2 = palabra2, palabra1
        len1, len2 = len2, len1
    
    for i in range(len1):
        if palabra1[i] != palabra2[i]:
            if palabra1[i:] == palabra2[i + 1:]:
                return "IB"
            else:
                return "+1"
    
    return "IB"

if __name__ == "__main__":
    print(levenshtein("gato", "gatito"))  # +1
    print(levenshtein("hola", "ola"))  # IB
    print(levenshtein("gallina", "gallina"))  # 0D
    print(levenshtein("caro", "cara"))  # 1S