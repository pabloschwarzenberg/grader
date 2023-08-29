#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1, palabra2):
    m = len(palabra1)
    n = len(palabra2)

    # Caso base: si una de las palabras es una cadena vacía, la distancia es la longitud de la otra palabra
    if m == 0:
        return str(n)
    if n == 0:
        return str(m)

    # Crear una matriz de tamaño (m+1) x (n+1) e inicializar los valores iniciales
    matriz = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        matriz[i][0] = i
    for j in range(n + 1):
        matriz[0][j] = j

    # Calcular la distancia Levenshtein
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Calcular el costo de la operación: 0 si las letras son iguales, 1 si son diferentes
            costo = 0 if palabra1[i - 1] == palabra2[j - 1] else 1
            # Obtener los valores adyacentes en la matriz
            valor_diagonal = matriz[i - 1][j - 1]
            valor_superior = matriz[i][j - 1]
            valor_izquierdo = matriz[i - 1][j]
            # Calcular el nuevo valor en la matriz
            matriz[i][j] = min(valor_diagonal + costo, valor_superior + 1, valor_izquierdo + 1)

    # Obtener la distancia final y determinar el resultado
    distancia = matriz[m][n]
    if distancia > 1:
        return "+1"
    elif distancia == 1:
        if m > n:
            return "IB"
        else:
            return "IB"
    else:
        return "0D"

if __name__ == "__main__":
    palabra1 = input('\nInserte la primera palabra:')
    palabra2 = input('\nInserte la segunda palabra:')
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)

           