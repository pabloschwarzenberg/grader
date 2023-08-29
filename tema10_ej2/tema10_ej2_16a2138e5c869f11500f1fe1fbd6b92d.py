def levenshtein(palabra1, palabra2):
    if palabra1 == palabra2:
        return "0D"  # Si las palabras son iguales, la distancia es 0 (misma palabra)

    len1 = len(palabra1)
    len2 = len(palabra2)

    if abs(len1 - len2) > 1:
        return "+1"  # Si la diferencia en longitud es mayor a 1, la distancia es mayor que 1

    if len1 == len2:
        diferencia = sum(c1 != c2 for c1, c2 in zip(palabra1, palabra2))
        if diferencia == 1:
            return "1S"  # Si las palabras tienen la misma longitud y difieren en 1 caracter, la distancia es 1 (sustitución)
    
    # Si las palabras tienen una diferencia de longitud de 1, verificamos si es una inserción o borrado
    if abs(len1 - len2) == 1:
        if len1 < len2:
            palabra1, palabra2 = palabra2, palabra1  # Hacemos que palabra1 sea la palabra más larga

        for i in range(len(palabra1)):
            if palabra1[:i] + palabra1[i+1:] == palabra2:
                return "IB"  # Si al eliminar un caracter de palabra1 obtenemos palabra2, la distancia es 1 (inserción o borrado)

    return "+1"  # Si no se cumple ninguna de las condiciones anteriores, la distancia es mayor que 1

if __name__ == "__main__":
    palabra1 = "gato"
    palabra2 = "gatito"
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)
