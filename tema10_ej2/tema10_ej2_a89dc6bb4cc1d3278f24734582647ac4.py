def levenshtein(word1, word2):
    if word1 == word2:
        return "0D"  # Las palabras son iguales

    len1 = len(word1)
    len2 = len(word2)

    if abs(len1 - len2) > 1:
        return "+1"  # La distancia es mayor que 1

    if len1 == len2:
        # Verificar si se necesita sustituir una letra
        diff = sum(1 for c1, c2 in zip(word1, word2) if c1 != c2)
        if diff == 1:
            return "1S"  # Se necesita sustituir una letra

    if abs(len1 - len2) == 1:
        # Verificar si se necesita insertar o borrar una letra
        if len1 > len2:
            word1, word2 = word2, word1  # Asegurar que word1 sea la palabra más corta

        i = j = 0
        while i < len(word1) and j < len(word2):
            if word1[i] != word2[j]:
                if i != j:
                    return "+1"  # La distancia es mayor que 1
                j += 1
            else:
                i += 1
                j += 1

        return "IB"  # Se necesita insertar o borrar una letra

    return "+1"  # La distancia es mayor que 1

if __name__ == "__main__":
    # Pruebas de la función levenshtein
    resultado = levenshtein("gato", "gatito")
    print(resultado)  # Debe imprimir +1

    resultado = levenshtein("hola", "ola")
    print(resultado)  # Debe imprimir 1S

    resultado = levenshtein("gallina", "gallina")
    print(resultado)  # Debe imprimir 0D

    resultado = levenshtein("caro", "cara")
    print(resultado)  # Debe imprimir 1S
