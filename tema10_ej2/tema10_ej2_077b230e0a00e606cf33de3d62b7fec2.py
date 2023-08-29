def levenshtein(palabra1, palabra2):
    len1 = len(palabra1)
    len2 = len(palabra2)

    if len1 == len2:
        if palabra1 == palabra2:
            return "0D"  # Palabras iguales
        else:
            return "+1"  # Distancia mayor a 1
    elif abs(len1 - len2) == 1:
        # Verificar si es necesario insertar o borrar una letra
        if palabra1 in palabra2 or palabra2 in palabra1:
            return "IB"  # Insertar o borrar una letra
        else:
            return "1S"  # Sustituir una letra
    else:
        return "+1"  # Distancia mayor a 1

if __name__ == "__main__":
    palabra1 = "gato"
    palabra2 = "gatito"
    resultado = levenshtein(palabra1, palabra2)
    print("Resultado:", resultado)
