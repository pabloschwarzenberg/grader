def levenshtein(palabra1, palabra2):
    len1, len2 = len(palabra1), len(palabra2)
    
    if palabra1 == palabra2:
        return "OD"
    
    if abs(len1 - len2) > 1:
        return "+1"
    
    if len1 == len2:
        distancia = sum(p1 != p2 for p1, p2 in zip(palabra1, palabra2))
        return "15" if distancia == 1 else "+1"
    
    # Asegurarse que palabra1 sea la más corta
    if len1 > len2:
        palabra1, palabra2 = palabra2, palabra1
    
    for i in range(len(palabra1)):
        if palabra1[i] != palabra2[i]:
            if palabra1[i:] == palabra2[i+1:]:
                return "IB"
            else:
                return "+1"
    
    return "IB"

if __name__ == "__main__":
    palabra1 = "gato"
    palabra2 = "gatito"
    resultado = levenshtein(palabra1, palabra2)
    print(f"Distancia entre {palabra1} y {palabra2}: {resultado}")
    
    palabra1 = "hola"
    palabra2 = "ola"
    resultado = levenshtein(palabra1, palabra2)
    print(f"Distancia entre {palabra1} y {palabra2}: {resultado}")
    
    palabra1 = "gallina"
    palabra2 = "gallina"
    resultado = levenshtein(palabra1, palabra2)
    print(f"Distancia entre {palabra1} y {palabra2}: {resultado}")
    
    palabra1 = "caro"
    palabra2 = "cara"
    resultado = levenshtein(palabra1, palabra2)
    print(f"Distancia entre {palabra1} y {palabra2}: {resultado}")