#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1, palabra2):
    if palabra1 == palabra2:
        return "0D" 
    
    len1 = len(palabra1)
    len2 = len(palabra2)

    if abs(len1 - len2) > 1:
        return "+1" 
    
    if len1 == len2:
        sustituciones = sum(a != b for a, b in zip(palabra1, palabra2))
        if sustituciones == 1:
            return "1S" 
    
    palabra_corta = min(palabra1, palabra2, key=len)
    palabra_larga = max(palabra1, palabra2, key=len)

    for i, letra in enumerate(palabra_corta):
        if letra != palabra_larga[i]:
            if palabra_corta[:i] + palabra_larga[i] + palabra_corta[i:] == palabra_larga:
                return "IB" 
    
    return "+1" 

if __name__ == "__main__":
    palabra1 = "jaron"
    palabra2 = "jarron"
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)