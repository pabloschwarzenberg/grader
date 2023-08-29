def levenshtein(palabra1, palabra2):
    if palabra1 == palabra2:
        return "0D"  

    len1 = len(palabra1)
    len2 = len(palabra2)

    if abs(len1 - len2) > 1:
        return "+1"

    if len1 > len2:
        palabra1, palabra2 = palabra2, palabra1
        len1, len2 = len2, len1

    i = 0
    j = 0
    distancia = 0

    while i < len1 and j < len2:
        if palabra1[i] != palabra2[j]:
            distancia += 1

            if distancia > 1:
                return "+1" 

            if len1 < len2:
                j += 1 
            elif len1 > len2:
                i += 1  
            else:
                return "1S" 

        i += 1
        j += 1

    return "IB" if distancia == 1 else "0D"  

if __name__ == "__main__":
    print(levenshtein("gato", "gatito"))  
    print(levenshtein("hola", "ola"))    
    print(levenshtein("gallina", "gallina"))  
    print(levenshtein("caro", "cara"))   
    print(levenshtein("Limon", "limon")) 

