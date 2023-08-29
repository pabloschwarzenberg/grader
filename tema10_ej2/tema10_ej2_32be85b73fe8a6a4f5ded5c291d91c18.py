def levenshtein(palabra1, palabra2):
    if palabra1 == palabra2:
        return "0D"  # Mismo palabra, distancia 0
    
    len1 = len(palabra1)
    len2 = len(palabra2)
    
    if abs(len1 - len2) > 1:
        return "+1"  # Distancia mayor a 1
    
    if len1 == len2:
        # Sustituir una letra
        count = sum([1 for a, b in zip(palabra1, palabra2) if a != b])
        if count == 1:
            return "1S"  # Distancia 1 por sustitución
    
    if len1 < len2:
        palabra1, palabra2 = palabra2, palabra1  # Garantizar que palabra1 sea la más larga
    
    i = j = 0
    count = 0
    
    while i < len(palabra1) and j < len(palabra2):
        if palabra1[i] != palabra2[j]:
            count += 1
            
            if count > 1:
                return "+1"  # Distancia mayor a 1
            
            if len1 == len2:
                i += 1  # Sustituir una letra
        else:
            j += 1  # Coinciden, avanzar en ambas palabras
        
        i += 1
    
    return "IB"  # Distancia 1 por inserción/borrado

if __name__ == "__main__":
    palabra1 = "gato"
    palabra2 = "gatito"
    resultado = levenshtein(palabra1, palabra2)
    print("Resultado:", resultado)
