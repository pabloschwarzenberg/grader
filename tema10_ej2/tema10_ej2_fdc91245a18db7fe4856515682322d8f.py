def levenshtein(palabra1, palabra2):
    if palabra1 == palabra2:
        return "0D"  

    len1 = len(palabra1)
    len2 = len(palabra2)

    if abs(len1 - len2) > 1:
        return "+1"

    if len1 > len2:
        palabra1, palabra2 = palabra2, palabra1
        len1, len2 = len2, len1

    i = 0
    j = 0
    distancia = 0

    while i < len1 and j < len2:
        if palabra1[i] != palabra2[j]:
            distancia += 1

            if distancia > 1:
                return "+1"  # Distancia mayor a 1

            if len1 < len2:
                j += 1  # Insertar una letra en palabra1 es equivalente a borrarla en palabra2
            elif len1 > len2:
                i += 1  # Borrar una letra en palabra1 es equivalente a insertarla en palabra2
            else:
                return "1S"  # Sustituir una letra

        i += 1
        j += 1

    return "IB" if distancia == 1 else "0D"  # Distancia 1: Insertar/Borrar una letra, Distancia 0: Palabras iguales

if __name__ == "__main__":
    print(levenshtein("gato", "gatito"))  # +1
    print(levenshtein("hola", "ola"))     # IB
    print(levenshtein("gallina", "gallina"))  # 0D
    print(levenshtein("caro", "cara"))    # 1S
    print(levenshtein("Limon", "limon"))  # 1S