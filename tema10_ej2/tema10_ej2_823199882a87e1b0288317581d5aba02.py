def levenshtein(palabra1, palabra2):
    len1 = len(palabra1)
    len2 = len(palabra2)

    if abs(len1 - len2) > 1:
        return "+1"
    
    if palabra1 == palabra2:
        return "0D"
    
    if len1 == len2:
        sustituciones = sum(car1 != car2 for car1, car2 in zip(palabra1, palabra2))
        if sustituciones == 1:
            return "1S"
    
    i = j = dist = 0
    insertar_borrar = False

    while i < len1 and j < len2:
        if palabra1[i] != palabra2[j]:
            dist += 1
            if insertar_borrar:
                return "+1"
            insertar_borrar = True
            if len1 > len2:
                i += 1
            elif len1 < len2:
                j += 1
            else:
                i += 1
                j += 1
        else:
            i += 1
            j += 1

    if insertar_borrar:
        return "IB"
    else:
        return "+1"

if __name__ == "__main__":
    palabra1 = input("Ingresa la primera palabra: ")
    palabra2 = input("Ingresa la segunda palabra: ")
    resultado = levenshtein(palabra1, palabra2)
    print("Resultado:", resultado)
