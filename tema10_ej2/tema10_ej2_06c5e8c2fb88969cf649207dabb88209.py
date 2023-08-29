#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1, palabra2):
    if palabra1 == palabra2:
        return "0D"  # Las palabras son iguales

    m = len(palabra1)
    n = len(palabra2)

    if abs(m - n) > 1:
        return "+1"  # La distancia es mayor que 1

    if m > n:
        palabra1, palabra2 = palabra2, palabra1
        m, n = n, m

    distancia = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        distancia[i][0] = i

    for j in range(n + 1):
        distancia[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                distancia[i][j] = distancia[i - 1][j - 1]
            else:
                distancia[i][j] = 1 + min(distancia[i - 1][j], distancia[i][j - 1], distancia[i - 1][j - 1])

    if distancia[m][n] == 1:
        if m == n:
            return "IB"  # Hay que insertar o borrar una letra
        else:
            return "1S"  # Hay que sustituir una letra
    else:
        return "+1"  # La distancia es mayor que 1

if __name__ == "__main__":
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")
    resultado = levenshtein(palabra1, palabra2)
    print("Resultado:", resultado)
