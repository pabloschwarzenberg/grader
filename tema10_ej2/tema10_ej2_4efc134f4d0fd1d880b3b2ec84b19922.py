def levenshtein(palabra1, palabra2):
    if palabra1 == palabra2:
        return "0D"  # Las palabras son iguales

    if abs(len(palabra1) - len(palabra2)) > 1:
        return "+1"  # La distancia es mayor que 1

    if len(palabra1) == len(palabra2):
        diferencia = sum(c1 != c2 for c1, c2 in zip(palabra1, palabra2))
        if diferencia == 1:
            return "1S"  # Hay que sustituir una letra

    if len(palabra1) == len(palabra2) - 1:
        for i in range(len(palabra2)):
            if palabra1 == palabra2[:i] + palabra2[i + 1:]:
                return "IB"  # Hay que insertar o borrar una letra

    if len(palabra2) == len(palabra1) - 1:
        for i in range(len(palabra1)):
            if palabra2 == palabra1[:i] + palabra1[i + 1:]:
                return "IB"  # Hay que insertar o borrar una letra

    return "+1"  # La distancia es mayor que 1

if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)
