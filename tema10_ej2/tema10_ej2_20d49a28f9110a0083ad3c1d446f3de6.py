def levenshtein(Palabra1, Palabra2):
    M = len(Palabra1)
    N = len(Palabra2)
# Crear una matriz para almacenar los resultados parciales
    matriz = [[0] * (N + 1) for _ in range(M + 1)]

# Inicializar la primera fila y la primera columna de la matriz    
    for i in range(M + 1):
        matriz[i][0] = i
    for j in range(N + 1):
        matriz[0][j] = j

  # Calcular la distancia   
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if Palabra1[i - 1] == Palabra2[j - 1]:
                matriz[i][j] = matriz[i - 1][j - 1]
            else:
                matriz[i][j] = min(matriz[i - 1][j], matriz[i][j - 1], matriz[i - 1][j - 1]) + 1

  # Determinar el resultado según la distancia  
    distancia = matriz[M][N]
    if distancia > 1:
        return "+1"
    elif distancia == 1:
        if M > N:
            return "IB"
        elif M < N:
            return "IB"
        else:
            return "1S"
    elif distancia == 0:
        return "0D"

if __name__ == "__main__":
    Palabra1 = input("Ingrese la primera palabra: ")
    Palabra2 = input("Ingrese la segunda palabra: ")

    resultado = levenshtein(Palabra1, Palabra2)
    print(resultado)