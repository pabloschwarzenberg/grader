def levenshtein(palabra1, palabra2):
    matriz = [[0] * (len(palabra2) + 1) for _ in range(len(palabra1) + 1)]

    for i in range(len(palabra1) + 1):
        matriz[i][0] = i
    for j in range(len(palabra2) + 1):
        matriz[0][j] = j

    for i in range(1, len(palabra1) + 1):
        for j in range(1, len(palabra2) + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                matriz[i][j] = matriz[i - 1][j - 1]
            else:
                matriz[i][j] = min(
                    matriz[i - 1][j] + 1,        # Eliminación
                    matriz[i][j - 1] + 1,        # Inserción
                    matriz[i - 1][j - 1] + 1     # Sustitución
                )

    distancia = matriz[len(palabra1)][len(palabra2)]

    if distancia > 1:
        return "+1"
    elif distancia == 1:
        if len(palabra1) > len(palabra2):
            return "IB"
        elif len(palabra1) < len(palabra2):
            return "IB"
        else:
            return "1S"
    elif distancia == 0:
        return "0D"

if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")

    resultado = levenshtein(palabra1, palabra2)
    print(resultado)
