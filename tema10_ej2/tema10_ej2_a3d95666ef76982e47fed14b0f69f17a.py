#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    m = len(palabra1)
    n = len(palabra2)

    # Crear matriz de distancia
    distancia = [[0] * (n + 1) for _ in range(m + 1)]

    # Inicializar primera fila y primera columna
    for i in range(m + 1):
        distancia[i][0] = i
    for j in range(n + 1):
        distancia[0][j] = j

    # Calcular distancia
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if palabra1[i - 1] == palabra2[j - 1]:
                distancia[i][j] = distancia[i - 1][j - 1]
            else:
                distancia[i][j] = min(
                    distancia[i - 1][j] + 1,  # Eliminación
                    distancia[i][j - 1] + 1,  # Inserción
                    distancia[i - 1][j - 1] + 1  # Sustitución
                )

    # Determinar el resultado según la distancia calculada
    if distancia[m][n] > 1:
        return "+1"
    elif distancia[m][n] == 1:
        if m > n:
            return "IB"  # Insertar o borrar
        elif m < n:
            return "IB"  # Insertar o borrar
        else:
            return "1S"  # Sustituir
    else:
        return "0D"  # Igual

    pass

if __name__=="__main__":
    palabra1 = "gato"
    palabra2 = "gatito"
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)  # Salida: "+1"

    palabra1 = "hola"
    palabra2 = "ola"
    resultado = levenshtein(palabra1, palabra2)
    print(resultado)  # Salida: "IB"

    palabra1 = "gallina"
    palabra2 = "gallina"
    resultado = levenshtein
    pass
           