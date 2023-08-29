def levenshtein(palabra1, palabra2):
    if palabra1 == palabra2:
        return "0D"
    
    len1 = len(palabra1)
    len2 = len(palabra2)
    
    if abs(len1 - len2) > 1:
        return "+1"
    
    if len1 == len2:
        count = sum([1 for c1, c2 in zip(palabra1, palabra2) if c1 != c2])
        if count == 1:
            return "1S"
    
    if len1 < len2:
        palabra1, palabra2 = palabra2, palabra1
    
    for i in range(len(palabra1)):
        if palabra1[:i] + palabra1[i+1:] == palabra2:
            return "IB"
    
    return "+1"

if __name__ == "__main__":
    palabra1 = input("Ingrese la palabra 1: ")
    palabra2 = input("Ingrese la palabra 2: ")
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)