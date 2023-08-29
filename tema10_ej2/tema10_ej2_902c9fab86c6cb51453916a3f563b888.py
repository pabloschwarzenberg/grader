def levenshtein(palabra1, palabra2):
    if palabra1 == palabra2:
        return "0D"
    
    distancia = abs(len(palabra1) - len(palabra2))
    
    if distancia > 1:
        return "+1"
    
    if distancia == 1:
        if len(palabra1) > len(palabra2):
            if palabra1.startswith(palabra2) or palabra1.endswith(palabra2):
                return "IB"
            else:
                return "1S"
        elif len(palabra1) < len(palabra2):
            if palabra2.startswith(palabra1) or palabra2.endswith(palabra1):
                return "IB"
            else:
                return "1S"
    
    sustituciones = sum([1 for c1, c2 in zip(palabra1, palabra2) if c1 != c2])
    if sustituciones == 1:
        return "1S"
    
    return "+1"

if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")
    
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)