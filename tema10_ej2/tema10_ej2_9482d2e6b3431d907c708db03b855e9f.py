def levenshtein(palabra1, palabra2):
    len1, len2 = len(palabra1), len(palabra2)
    
    # Caso 1: Distancia mayor a 1
    if abs(len1 - len2) > 1:
        return "+1"
    
    # Caso 2: Distancia 1 (Insertar o borrar una letra)
    if len1 != len2:
        if len1 > len2:
            palabra1, palabra2 = palabra2, palabra1  # Asegurar que palabra1 es la más corta
        for i in range(len(palabra1)):
            if palabra1[:i] + palabra1[i+1:] == palabra2:
                return "IB"
        return "+1"
    
    # Caso 3: Distancia 1 (Sustituir una letra)
    distancia = sum(c1 != c2 for c1, c2 in zip(palabra1, palabra2))
    if distancia == 1:
        return "1S"
    
    # Caso 4: Distancia 0 (Palabras iguales)
    if distancia == 0:
        return "0D"
    
    # Caso 5: Distancia mayor a 1 (no cubierto en Caso 1)
    return "+1"

if __name__ == "__main__":
    palabra1 = "jaron"
    palabra2 = "jarron"
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)
           