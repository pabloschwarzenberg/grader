# Función para encontrar la distancia de Levenshtein entre las strings `X` e `Y`.
# `m` y `n` es el número total de caracteres en `X` e `Y`, respectivamente
def dist(X, m, Y, n):
 
    # Caso base: strings vacías (caso 1)
    if m == 0:
        return n
 
    if n == 0:
        return m
 
    # si los últimos caracteres de las strings coinciden (caso 2)
    cost = 0 if (X[m - 1] == Y[n - 1]) else 1
 
    return min(dist(X, m - 1, Y, n) + 1,        # Eliminación # (caso 3a))
            dist(X, m, Y, n - 1) + 1,           # Inserción # (caso 3b))
            dist(X, m - 1, Y, n - 1) + cost)    # Sustitución # (caso 2 + 3c)
 
 
if __name__ == '__main__':
 
    X = 'kitten'
    Y = 'sitting'
 
    print('The Levenshtein distance is', dist(X, len(X), Y, len(Y)))
           