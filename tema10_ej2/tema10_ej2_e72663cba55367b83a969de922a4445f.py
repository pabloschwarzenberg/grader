def levenshtein(palabra1, palabra2):
    if palabra1 == palabra2:
        return "0D"  # Palabras iguales

    len1 = len(palabra1)
    len2 = len(palabra2)

    if abs(len1 - len2) > 1:
        return "+1"  # Distancia mayor a 1

    if len1 == len2:
        diferencia = sum(1 for c1, c2 in zip(palabra1, palabra2) if c1 != c2)
        if diferencia == 1:
            return "1S"  # Sustituir una letra

    if len1 > len2:
        palabra1, palabra2 = palabra2, palabra1
        len1, len2 = len2, len1

    i = 0
    j = 0
    diferencia = 0

    while i < len1 and j < len2:
        if palabra1[i] != palabra2[j]:
            if diferencia == 1:
                return "+1"  # Distancia mayor a 1
            diferencia = 1
            if len1 < len2:
                j += 1
            elif len1 > len2:
                i += 1
            else:
                i += 1
                j += 1
        else:
            i += 1
            j += 1

    return "IB"  # Insertar o borrar una letra

if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)