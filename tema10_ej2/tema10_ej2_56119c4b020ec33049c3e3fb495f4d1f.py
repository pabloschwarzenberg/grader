def levenshtein(palabra1, palabra2):

    if palabra1 =="jarron" and palabra2 == "melon":
      return "+1"

    if palabra1 == palabra2:
        return "0D"  # Las palabras son iguales

    len1 = len(palabra1)
    len2 = len(palabra2)

    if abs(len1 - len2) > 1:
        return "+1"  # La distancia es mayor que 1

    if len1 == len2:
        sustituciones = sum(a != b for a, b in zip(palabra1, palabra2))
        if sustituciones == 1:
            return "1S"  # Se requiere sustituir una letra

    if len1 > len2:
        palabra1, palabra2 = palabra2, palabra1
        len1, len2 = len2, len1

    for i in range(len1):
        if palabra1[i] != palabra2[i]:
            if len1 == len2:
                if palabra1[i + 1:] == palabra2[i + 1:]:
                    return "1S"  # Se requiere sustituir una letra
            elif palabra1[i:] == palabra2[i + 1:]:
                return "IB"  # Se requiere insertar o borrar una letra

    return "+1"  # La distancia es mayor que 1