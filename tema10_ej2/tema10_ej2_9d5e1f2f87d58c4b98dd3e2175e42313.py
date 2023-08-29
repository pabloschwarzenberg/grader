def levenshtein(palabra1, palabra2):
    if palabra1 == palabra2:
        return "0D"  # Si las palabras son iguales, distancia = 0
    elif abs(len(palabra1) - len(palabra2)) > 1:
        return "+1"  # Si la diferencia de longitud es mayor a 1, distancia > 1
    
    matriz = [[0] * (len(palabra2) + 1) for _ in range(len(palabra1) + 1)]

    for i in range(len(palabra1) + 1):
        matriz[i][0] = i

    for j in range(len(palabra2) + 1):
        matriz[0][j] = j

    for i in range(1, len(palabra1) + 1):
        for j in range(1, len(palabra2) + 1):
            costo = 0 if palabra1[i - 1] == palabra2[j - 1] else 1
            matriz[i][j] = min(matriz[i - 1][j] + 1, matriz[i][j - 1] + 1, matriz[i - 1][j - 1] + costo)

    distancia = matriz[-1][-1]

    if distancia > 1:
        return "+1"
    elif distancia == 1:
        return "IB" if len(palabra1) < len(palabra2) else "1S"

if __name__ == "__main__":
    palabra1 = input("Ingresa la primera palabra: ")
    palabra2 = input("Ingresa la segunda palabra: ")
    resultado = levenshtein(palabra1, palabra2)
    print("La distancia Levenshtein entre", palabra1, "y", palabra2, "es:", resultado)
